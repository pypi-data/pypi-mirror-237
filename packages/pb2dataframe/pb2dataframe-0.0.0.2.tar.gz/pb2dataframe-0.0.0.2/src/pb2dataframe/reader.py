from __future__ import annotations

import base64
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, Generator, Type

import pandas as pd
from google.protobuf.descriptor import Descriptor, FieldDescriptor
from google.protobuf.descriptor_pb2 import FieldDescriptorProto
from google.protobuf.message import Message

DEFAULT_SKIP_NESTED = False
DEFAULT_DTYPE_ENUMERATED = "uint64"
DEFAULT_CHUNK_SIZE = 10000
DEFAULT_BYTES = base64.b16encode(b"").decode("utf-8").lower()

MAPPING_PROTOBUF_TO_PANDAS = {
    "TYPE_DOUBLE": "float64",
    "TYPE_FLOAT": "float32",
    "TYPE_INT64": "int64",
    "TYPE_UINT64": "uint64",
    "TYPE_INT32": "int32",
    "TYPE_FIXED64": "int64",
    "TYPE_FIXED32": "int32",
    "TYPE_BOOL": "bool",
    "TYPE_STRING": "object",
    "TYPE_GROUP": "object",
    "TYPE_MESSAGE": "object",
    "TYPE_BYTES": "object",
    "TYPE_UINT32": "uint32",
    "TYPE_ENUM": "category",
    "TYPE_SFIXED32": "int32",
    "TYPE_SFIXED64": "int64",
    "TYPE_SINT32": "int32",
    "TYPE_SINT64": "int64",
}


class KeyType(Enum):
    REPEATED_MESSAGE = 1
    REPEATED_SCALAR = 2
    SIMPLE_MESSAGE = 3
    MAP_VALUE_MESSAGE = 4
    MAP_VALUE_SCALAR = 5


@dataclass
class ProtobufStep:
    key: str
    foreign_key: str | None = None
    enumerate: bool = False
    enumerate_offset: int = 0


class ProtobufPath:
    steps: list[ProtobufStep]

    def __init__(self, steps=None) -> None:
        if steps:
            if not isinstance(steps, list):
                raise ValueError("No list provided for steps")
            else:
                for step in steps:
                    if not isinstance(step, ProtobufStep):
                        raise ValueError("step is not a ProtobufStep")

            self.steps = steps
        else:
            self.steps = []

    def add_step(
        self,
        key: str,
        foreign_key: str | None = None,
        enumerate: bool = False,
        enumerate_offset: int = 0,
    ) -> None:
        self.steps.append(ProtobufStep(key, foreign_key, enumerate, enumerate_offset))

    def go_forward(self) -> ProtobufPath:
        return ProtobufPath(steps=self.steps[1:])

    @property
    def step_current(self) -> ProtobufStep | None:
        if len(self.steps) > 0:
            return self.steps[0]
        return None


@dataclass
class ProtobufFieldStructure:
    key: Key | None = None
    fields_repeated_scalars: list[FieldDescriptor] | None = None
    fields_nested_messages_skiped: list[FieldDescriptor] | None = None
    fields_nested_messages: dict[FieldDescriptor, ProtobufFieldStructure] | None = None
    fields_enums: list[FieldDescriptor] | None = None
    fields_bytes: list[FieldDescriptor] | None = None
    fields_scalars: list[FieldDescriptor] | None = None


@dataclass
class Key:
    name: str
    structure: ProtobufFieldStructure | None
    field_descriptor: FieldDescriptor
    type: KeyType | None
    foreign_key_descriptor: FieldDescriptor | None
    enumerate: bool
    enumerate_offset: int = 0


def _cast_scalar(data) -> str:
    if isinstance(data, bytes):
        return base64.b16encode(data).decode("utf-8").lower()
    else:
        return data


def _cast_bytes(data) -> str:
    if data:
        return base64.b16encode(data).decode("utf-8").lower()
    else:
        return DEFAULT_BYTES


def _get_scalar_value(message: Message, field: FieldDescriptor) -> str | None:
    if field.type == field.TYPE_BYTES:
        return _cast_bytes(getattr(message, field.name, None))
    else:
        return getattr(message, field.name, None)


def _get_field_structure(
    descriptor: Descriptor, skip_nested: bool, path: ProtobufPath
) -> ProtobufFieldStructure:
    field_structure: ProtobufFieldStructure

    step_current = path.step_current
    subpath = path.go_forward()

    list_fields: list[FieldDescriptor]
    if step_current:
        list_fields = [descriptor.fields_by_name[step_current.key]]
    else:
        list_fields = descriptor.fields

    field_structure = ProtobufFieldStructure()
    key_type: KeyType | None = None
    key_field_structure: ProtobufFieldStructure | None = None

    field: FieldDescriptor
    for field in list_fields:
        if field.message_type is None:
            # message_type is None in the case of repeated and non-repeated
            # scalars. We are interested in repeated scalars only.

            # If it is not the last step and the field is repeated we are going
            # deeper. If it is the last, we are only interested in non-reapeted
            # fields.

            if step_current and field.label == field.LABEL_REPEATED:
                if field_structure.fields_repeated_scalars is None:
                    field_structure.fields_repeated_scalars = []
                field_structure.fields_repeated_scalars.append(field)
                key_type = KeyType.REPEATED_SCALAR

            elif not step_current and field.label != field.LABEL_REPEATED:
                # We are putting the field to list for the relevant scalar.

                if field.type == field.TYPE_BYTES:
                    if field_structure.fields_bytes is None:
                        field_structure.fields_bytes = []
                    field_structure.fields_bytes.append(field)

                elif field.type == field.TYPE_ENUM:
                    if field_structure.fields_enums is None:
                        field_structure.fields_enums = []
                    field_structure.fields_enums.append(field)

                else:
                    if field_structure.fields_scalars is None:
                        field_structure.fields_scalars = []
                    field_structure.fields_scalars.append(field)

        elif field.message_type.has_options and field.label == field.LABEL_REPEATED:
            # In case of a map we differ between messages and scalars on the
            # value field.

            # In protobuf, map is implemented as a repeated field of an
            # autogenerated message. This autogenerated message will have
            # two fields: 'key' and 'value'. We want to get the descriptor for
            # the 'value' field.
            value_field: FieldDescriptor = field.message_type.fields_by_name["value"]

            if step_current and value_field.type == value_field.TYPE_MESSAGE:
                key_field_structure = _get_field_structure(
                    value_field.message_type, skip_nested, subpath
                )
                key_type = KeyType.MAP_VALUE_MESSAGE

            elif step_current:
                key_type = KeyType.MAP_VALUE_SCALAR

        elif field.label == field.LABEL_REPEATED and field.type == field.TYPE_MESSAGE:
            # We are going deeper if it is not the last step of the path.
            # Otherwise we ignore the field.
            if step_current:
                key_field_structure = _get_field_structure(
                    field.message_type, skip_nested, subpath
                )
                key_type = KeyType.REPEATED_MESSAGE

        elif field.type == field.TYPE_MESSAGE:
            # We are going deeper if it os not the last step of the path.
            # Otherwise we are flattening the field only if skip_nested is not set.

            if step_current or skip_nested is False:
                if field_structure.fields_nested_messages is None:
                    field_structure.fields_nested_messages = {}

                field_structure.fields_nested_messages.update(
                    {
                        field: _get_field_structure(
                            field.message_type, skip_nested, subpath
                        )
                    }
                )

                key_type = KeyType.SIMPLE_MESSAGE

            elif not step_current and skip_nested is True:
                if field_structure.fields_nested_messages_skiped is None:
                    field_structure.fields_nested_messages_skiped = []
                field_structure.fields_nested_messages_skiped.append(field)

            if step_current:
                key_field_structure = _get_field_structure(
                    field.message_type, skip_nested, subpath
                )
                key_type = KeyType.SIMPLE_MESSAGE

        else:
            raise NotImplementedError(f"Case for field '{field.name}' not implemented")

    step_current = path.step_current

    if step_current:
        field_structure.key = Key(
            name=step_current.key,
            field_descriptor=descriptor.fields_by_name[step_current.key],
            structure=key_field_structure,
            foreign_key_descriptor=(
                descriptor.fields_by_name[step_current.foreign_key]
                if step_current.foreign_key
                else None
            ),
            type=key_type,
            enumerate=step_current.enumerate,
            enumerate_offset=step_current.enumerate_offset,
        )

    return field_structure


def _interpret_message(
    message: Message,
    field_structure: ProtobufFieldStructure,
    prefix_field_name: str = "",
) -> dict[str, Any]:
    data = {}  # default to dict
    field: FieldDescriptor

    if field_structure.fields_nested_messages_skiped is not None:
        for field in field_structure.fields_nested_messages_skiped:
            data[prefix_field_name + field.name] = "<object>"

    if field_structure.fields_nested_messages is not None:
        for field, fs in field_structure.fields_nested_messages.items():
            data.update(
                _interpret_message(
                    message=getattr(message, field.name),
                    field_structure=fs,
                    prefix_field_name=prefix_field_name + field.name + ".",
                )
            )

    if field_structure.fields_scalars is not None:
        for field in field_structure.fields_scalars:
            data[prefix_field_name + field.name] = getattr(message, field.name, None)

    if field_structure.fields_bytes is not None:
        for field in field_structure.fields_bytes:
            data[prefix_field_name + field.name] = _cast_bytes(
                getattr(message, field.name, None)
            )

    if field_structure.fields_enums is not None:
        for field in field_structure.fields_enums:
            field_data = getattr(message, field.name, None)
            data[prefix_field_name + field.name] = field.enum_type.values_by_number[
                field_data
            ].name

    return data


def _finalize_data(
    data: dict,
    foreign_key_dict: dict,
    enumerator: Generator[dict[str, int], None, None],
) -> dict:
    data.update(foreign_key_dict)
    data.update(next(enumerator))
    return data


def _create_enumerator(
    field_name: str | None, offset: int = 0
) -> Generator[dict[str, int], None, None]:
    i = offset
    if field_name is None:
        while True:
            yield {}
    else:
        while True:
            i += 1
            yield {field_name: i}


def _create_data_iterator(
    message: Message, field_structure: ProtobufFieldStructure
) -> Generator[dict[str, Any], None, None]:
    data: dict

    if field_structure.key is None:
        # This is case is only relevant if the first level of a message has to
        # be interpreted
        data = _interpret_message(message, field_structure)
        yield data

    else:
        key_field = field_structure.key.field_descriptor
        keydict: dict = {}
        if field_structure.key.foreign_key_descriptor:
            keydict[field_structure.key.foreign_key_descriptor.name] = (
                _get_scalar_value(message, field_structure.key.foreign_key_descriptor)
            )

        if field_structure.key.enumerate:
            enumerator = _create_enumerator(
                field_structure.key.field_descriptor.name + "_id",
                field_structure.key.enumerate_offset,
            )
        else:
            enumerator = _create_enumerator(None)

        if key_field.label == key_field.LABEL_REPEATED:
            messages = getattr(message, key_field.name)
        else:
            messages = [getattr(message, key_field.name)]

        if field_structure.key.type == KeyType.REPEATED_MESSAGE:
            if field_structure.key.structure is not None:
                if (
                    field_structure.key.structure.key is not None
                    and field_structure.key.structure.key.structure is None
                    and field_structure.key.structure.key.type
                    not in [
                        KeyType.MAP_VALUE_MESSAGE,
                        KeyType.MAP_VALUE_SCALAR,
                    ]
                ):
                    for m in messages:
                        data = _interpret_message(m, field_structure.key.structure)
                        yield _finalize_data(data, keydict, enumerator)

                else:
                    for m in messages:
                        for data in _create_data_iterator(
                            m, field_structure.key.structure
                        ):
                            yield _finalize_data(data, keydict, enumerator)

        elif (
            field_structure.key.type == KeyType.SIMPLE_MESSAGE
            and field_structure.key.structure is not None
        ):
            for m in messages:
                for data in _create_data_iterator(m, field_structure.key.structure):
                    yield _finalize_data(data, keydict, enumerator)

        elif field_structure.key.type == KeyType.MAP_VALUE_SCALAR:
            for m in messages:
                data = {}
                data[key_field.name + "_key"] = m
                data["value"] = _cast_scalar(messages[m])
                yield _finalize_data(data, keydict, enumerator)

        elif (
            field_structure.key.type == KeyType.MAP_VALUE_MESSAGE
            and field_structure.key.structure is not None
        ):
            for m in messages:
                data = _interpret_message(messages[m], field_structure.key.structure)
                data[key_field.name + "_key"] = m
                yield _finalize_data(data, keydict, enumerator)

        elif field_structure.key.type == KeyType.REPEATED_SCALAR:
            field: FieldDescriptor = field_structure.key.field_descriptor
            if field.type == field.TYPE_BYTES:
                for m in messages:
                    data = {}
                    data[field.name] = _cast_bytes(m)
                    yield _finalize_data(data, keydict, enumerator)

            else:
                for m in messages:
                    data = {}
                    data[field.name] = m
                    yield _finalize_data(data, keydict, enumerator)


def _create_dict_chunker(
    dict_generator: Generator[dict, None, None],
    chunksize: int = DEFAULT_CHUNK_SIZE,
) -> Generator[list[dict], None, None]:
    while True:
        chunk = []
        for _ in range(chunksize):
            try:
                data = next(dict_generator)
                chunk.append(data)
            except StopIteration:
                break

        if len(chunk) == 0:
            break

        yield chunk


def _get_field_dtype(field: FieldDescriptor) -> str:
    return MAPPING_PROTOBUF_TO_PANDAS[FieldDescriptorProto.Type.Name(field.type)]


def _get_pandas_dtypes(
    descriptor: Descriptor,
    field_structure: ProtobufFieldStructure,
    prefix_field_name: str = "",
) -> dict[str, Any]:
    dtypes: dict[str, str] = {}

    if field_structure.key:
        subdescriptor: Descriptor = field_structure.key.field_descriptor.message_type

        if (
            field_structure.key.type == KeyType.REPEATED_MESSAGE
            and field_structure.key.structure is not None
        ):
            dtypes.update(
                _get_pandas_dtypes(subdescriptor, field_structure.key.structure)
            )

        elif (
            field_structure.key.type == KeyType.SIMPLE_MESSAGE
            and field_structure.key.structure is not None
        ):
            dtypes.update(
                _get_pandas_dtypes(subdescriptor, field_structure.key.structure)
            )

        elif field_structure.key.type == KeyType.MAP_VALUE_SCALAR:
            dtypes[field_structure.key.field_descriptor.name + "_key"] = (
                _get_field_dtype(
                    field_structure.key.field_descriptor.message_type.fields_by_name[
                        "key"
                    ]
                )
            )
            dtypes["value"] = _get_field_dtype(
                field_structure.key.field_descriptor.message_type.fields_by_name[
                    "value"
                ]
            )

        elif (
            field_structure.key.type == KeyType.MAP_VALUE_MESSAGE
            and field_structure.key.structure is not None
        ):
            dtypes[field_structure.key.field_descriptor.name + "_key"] = (
                _get_field_dtype(
                    field_structure.key.field_descriptor.message_type.fields_by_name[
                        "key"
                    ]
                )
            )
            dtypes.update(
                _get_pandas_dtypes(subdescriptor, field_structure.key.structure)
            )

        if field_structure.key.foreign_key_descriptor:
            dtypes[field_structure.key.foreign_key_descriptor.name] = _get_field_dtype(
                descriptor.fields_by_name[
                    field_structure.key.foreign_key_descriptor.name
                ]
            )

        if field_structure.key.enumerate:
            dtypes[field_structure.key.field_descriptor.name + "_id"] = (
                DEFAULT_DTYPE_ENUMERATED
            )

    else:
        field: FieldDescriptor
        if field_structure.fields_nested_messages_skiped is not None:
            for field in field_structure.fields_nested_messages_skiped:
                dtypes[prefix_field_name + field.name] = "object"

        if field_structure.fields_nested_messages is not None:
            for field, fs in field_structure.fields_nested_messages.items():
                dtypes.update(
                    _get_pandas_dtypes(
                        descriptor=field.message_type,
                        field_structure=fs,
                        prefix_field_name=prefix_field_name + field.name + ".",
                    )
                )

        if field_structure.fields_scalars is not None:
            for field in field_structure.fields_scalars:
                dtypes[prefix_field_name + field.name] = _get_field_dtype(field)

        if field_structure.fields_bytes is not None:
            for field in field_structure.fields_bytes:
                dtypes[prefix_field_name + field.name] = _get_field_dtype(field)

        if field_structure.fields_enums is not None:
            for field in field_structure.fields_enums:
                dtypes[prefix_field_name + field.name] = _get_field_dtype(field)

    return dtypes


def create_message_generator(
    func: Callable[..., Message],
    grpc_max_responses: int,
    field_response_data: str,
    field_response_last_index: str,
    field_request_max: str,
    field_request_offset: str,
    **kwargs,
) -> Generator[Message, None, None]:
    kwargs_request = deepcopy(kwargs)
    kwargs_request[field_request_max] = grpc_max_responses

    requests_open = kwargs.get(field_request_max)

    while True:
        if requests_open is not None and requests_open < grpc_max_responses:
            kwargs_request[field_request_max] = requests_open

        response: Message = func(**kwargs_request)

        yield response

        len_data = len(getattr(response, field_response_data))

        if len_data < grpc_max_responses:
            break

        if requests_open is not None:
            requests_open -= len_data
            if requests_open == 0:
                break

        kwargs_request[field_request_offset] = getattr(
            response, field_response_last_index
        )


def messages_to_pandas(
    messages: Message | list[Message] | Generator[Message, None, None],
    message_type: Type[Any | Message],
    paths: list[ProtobufPath],
    skip_nested: bool = DEFAULT_SKIP_NESTED,
) -> list[pd.DataFrame]:
    # If messages is a Message or a list[Message] we convert it in a generator
    # of Messages.
    if isinstance(messages, Generator):
        pass
    elif isinstance(messages, Message):
        messages = (m for m in [messages])
    elif isinstance(messages, list):
        messages = (m for m in messages)
    else:
        raise ValueError(
            "message isn't a protobuf.Message or a list or a generator of messages"
        )

    dataframe_chunks: list[list[pd.DataFrame]] = [[] for _ in paths]
    field_structures: list[ProtobufFieldStructure] = []

    for path in paths:
        if isinstance(path, ProtobufPath):
            field_structures.append(
                _get_field_structure(message_type.DESCRIPTOR, skip_nested, path)
            )
        else:
            raise ValueError("path is not a ProtobufPath")

    message: Message
    for message in messages:
        # Check that message is not empty
        if not message:
            continue

        if not isinstance(message, Message):
            raise ValueError("Element of the list is not a protobuf.Message")

        if not message_type().DESCRIPTOR.full_name == message.DESCRIPTOR.full_name:
            raise ValueError(
                f"message is not of type {message_type().DESCRIPTOR.full_name}"
            )

        for i, field_structure in enumerate(field_structures):
            if field_structure is not None:
                for chunk in _create_dict_chunker(
                    _create_data_iterator(message, field_structure)
                ):
                    dataframe_chunks[i].append(pd.DataFrame(chunk))
                    if field_structure.key and field_structure.key.enumerate:
                        field_structure.key.enumerate_offset += len(
                            getattr(message, field_structure.key.name)
                        )

    result: list[pd.DataFrame] = []

    for i, field_structure in enumerate(field_structures):
        dtypes = _get_pandas_dtypes(message_type.DESCRIPTOR, field_structure)

        if len(dataframe_chunks) == 0 or len(dataframe_chunks[i]) == 0:
            result.append(
                pd.DataFrame(columns=list(dtypes.keys())).astype(dtype=dtypes)
            )
        else:
            chunks_converted: list[pd.DataFrame] = []

            while dataframe_chunks[i]:
                chunks_converted.append(dataframe_chunks[i].pop(0).astype(dtype=dtypes))

            result.append(pd.concat(chunks_converted, ignore_index=True))

    return result
