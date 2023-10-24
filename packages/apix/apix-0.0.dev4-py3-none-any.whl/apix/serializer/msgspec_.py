import typing
import msgspec

from ..proto import T
from ..dto import PathInfo
from .base import BasePath


class MsgspecSchema(msgspec.Struct): ...


class MsgspecPath(msgspec.Struct, typing.Generic[T]):
    __info__: typing.ClassVar[PathInfo] = PathInfo()
    build_request = BasePath.build_request
    build_result = BasePath.build_result


class MsgspecSerializer:
    def __init__(self) -> None:
        self.__encoder = msgspec.json.Encoder()
    
    def encode(self, obj) -> bytes:
        return self.__encoder.encode(obj)

    def decode(self, data, type: typing.Type[T]) -> T:
        print(data, type)
        return msgspec.json.decode(data, type=type)

    def encode_fields(self, obj) -> typing.Dict[str, typing.Any]:
        # if issubclass(obj.__class__, MsgspecPath):
        #     return {
        #                 f.name: self.encode(getattr(obj, f.name))
        #                 for f in msgspec.structs.fields(obj)
        #             }
        return msgspec.to_builtins(obj)