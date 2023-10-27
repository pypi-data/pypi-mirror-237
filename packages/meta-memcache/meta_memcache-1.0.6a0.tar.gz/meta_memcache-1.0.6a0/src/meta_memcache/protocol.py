from dataclasses import dataclass

from enum import Enum, IntEnum
from typing import (
    Any,
    Dict,
    List,
    Optional,
    Set,
    Union,
)


ENDL = b"\r\n"
NOOP: bytes = b"mn" + ENDL
ENDL_LEN = 2
SPACE: int = ord(" ")

Blob = Union[bytes, bytearray, memoryview]


@dataclass(slots=True, init=False, unsafe_hash=True)
class Key:
    key: str
    routing_key: Optional[str]
    is_unicode: bool

    def __init__(
        self,
        key: str,
        routing_key: Optional[str] = None,
        is_unicode: bool = False,
    ) -> None:
        self.key = key
        self.routing_key = routing_key
        self.is_unicode = is_unicode


# class Key(NamedTuple):
#     key: str
#     routing_key: Optional[str] = None
#     is_unicode: bool = False


class MetaCommand(Enum):
    META_GET = b"mg"  # Meta Get
    META_SET = b"ms"  # Meta Set
    META_DELETE = b"md"  # Meta Delete
    META_ARITHMETIC = b"ma"  # Meta Arithmetic


class SetMode(Enum):
    SET = b"S"  # Default
    ADD = b"E"  # Add if item does NOT EXIST, else LRU bump and return NS
    APPEND = b"A"  # If item exists, append the new value to its data.
    PREPEND = b"P"  # If item exists, prepend the new value to its data.
    REPLACE = b"R"  # Set only if item already exists.


class Flag(Enum):
    BINARY = b"b"
    NOREPLY = b"q"
    RETURN_CLIENT_FLAG = b"f"
    RETURN_CAS_TOKEN = b"c"
    RETURN_VALUE = b"v"
    RETURN_TTL = b"t"
    RETURN_SIZE = b"s"
    RETURN_LAST_ACCESS = b"l"
    RETURN_FETCHED = b"h"
    RETURN_KEY = b"k"
    NO_UPDATE_LRU = b"u"
    # WIN = b"W"
    # LOST = b"Z"
    # STALE = b"X"
    MARK_STALE = b"I"


class IntFlag(Enum):
    # TTL = b"t"
    CACHE_TTL = b"T"
    RECACHE_TTL = b"R"
    MISS_LEASE_TTL = b"N"
    # CLIENT_FLAG = b"f"
    SET_CLIENT_FLAG = b"F"
    # LAST_READ_AGE = b"l"
    # HIT_AFTER_WRITE = b"h"
    MA_INITIAL_VALUE = b"J"
    MA_DELTA_VALUE = b"D"
    # RETURNED_CAS_TOKEN = b"c"
    CAS_TOKEN = b"C"


class TokenFlag(Enum):
    OPAQUE = b"O"
    # KEY = b"k"
    # 'M' (mode switch):
    # * Meta Arithmetic:
    #  - I or +: increment
    #  - D or -: decrement
    # * Meta Set: See SetMode Enum above
    #  - E: "add" command. LRU bump and return NS if item exists. Else add.
    #  - A: "append" command. If item exists, append the new value to its data.
    #  - P: "prepend" command. If item exists, prepend the new value to its data.
    #  - R: "replace" command. Set only if item already exists.
    #  - S: "set" command. The default mode, added for completeness.
    MODE = b"M"


# Store maps of byte values (int) to enum value
flag_values: Dict[int, Flag] = {f.value[0]: f for f in Flag}
int_flags_values: Dict[int, IntFlag] = {f.value[0]: f for f in IntFlag}
token_flags_values: Dict[int, TokenFlag] = {f.value[0]: f for f in TokenFlag}

DEFAULT_FLAGS: Set[Flag] = {
    Flag.RETURN_VALUE,
    Flag.RETURN_TTL,
    Flag.RETURN_CLIENT_FLAG,
    Flag.RETURN_LAST_ACCESS,
    Flag.RETURN_FETCHED,
}
DEFAULT_FLAGS_AS_BYTES = b" ".join(flag.value for flag in DEFAULT_FLAGS)
DEFAULT_CAS_FLAGS: Set[Flag] = {
    Flag.RETURN_VALUE,
    Flag.RETURN_TTL,
    Flag.RETURN_CLIENT_FLAG,
    Flag.RETURN_LAST_ACCESS,
    Flag.RETURN_FETCHED,
    Flag.RETURN_CAS_TOKEN,
}
DEFAULT_CAS_FLAGS_AS_BYTES = b" ".join(flag.value for flag in DEFAULT_CAS_FLAGS)


@dataclass
class MemcacheResponse:
    __slots__ = ()


@dataclass
class Miss(MemcacheResponse):
    __slots__ = ()

    pass


# def _get_flag_positions(header: Blob, pos: int = 3) -> List[int]:
#     header_size = len(header)
#     positions = []
#     while pos < header_size:
#         if header[pos] == SPACE:
#             pos += 1
#             continue
#         # Flag start
#         positions.append(pos)
#         # Advance to the end of the flag:
#         for i in range(pos + 1, header_size):
#             if header[i] == SPACE:
#                 break
#         pos = i + 1
#     return positions


# def _get_size_and_flag_positions(header: Blob) -> Tuple[int, List[int]]:
#     header_size = len(header)
#     if header_size >= 4 and header[2] == SPACE:
#         end = header_size
#         for i in range(4, header_size):
#             if header[i] == SPACE:
#                 end = i
#                 break
#         size = int(header[3:end])
#         return size, _get_flag_positions(header, pos=end + 1)
#     raise ValueError(f"Invalid header {header!r}")

# Response flags
TOKEN_FLAG_OPAQUE = ord("O")
INT_FLAG_CAS_TOKEN = ord("c")
INT_FLAG_FETCHED = ord("h")
INT_FLAG_LAST_ACCESS = ord("l")
INT_FLAG_TTL = ord("t")
INT_FLAG_CLIENT_FLAG = ord("f")
INT_FLAG_SIZE = ord("s")
FLAG_WIN = ord("W")
FLAG_LOST = ord("Z")
FLAG_STALE = ord("X")


@dataclass(slots=True, init=False)
class Success(MemcacheResponse):
    # __slots__ = (
    #     "cas_token",
    #     "fetched",
    #     "last_access",
    #     "ttl",
    #     "client_flag",
    #     "win",
    #     "stale",
    #     "real_size",
    #     "opaque",
    # )
    cas_token: Optional[int]
    fetched: Optional[int]
    last_access: Optional[int]
    ttl: Optional[int]
    client_flag: Optional[int]
    win: Optional[bool]
    stale: Optional[bool]
    real_size: Optional[int]
    opaque: Optional[bytes]

    def __init__(
        self,
        *,
        cas_token: Optional[int] = None,
        fetched: Optional[int] = None,
        last_access: Optional[int] = None,
        ttl: Optional[int] = None,
        client_flag: Optional[int] = None,
        win: Optional[bool] = None,
        stale: Optional[bool] = None,
        real_size: Optional[int] = None,
        opaque: Optional[bytes] = None,
    ) -> None:
        self.cas_token = cas_token
        self.fetched = fetched
        self.last_access = last_access
        self.ttl = ttl
        self.client_flag = client_flag
        self.win = win
        self.stale = stale
        self.real_size = real_size
        self.opaque = opaque

    @classmethod
    def from_header(cls, header: Blob) -> "Success":
        result = cls()
        result._set_flags(header)
        return result

    def _set_flags(self, header: bytes, pos: int = 3) -> None:  # noqa: C901
        header_size = len(header)
        while pos < header_size:
            flag = header[pos]
            pos += 1
            if flag == SPACE:
                continue
            # space_pos = header.find(SPACE, pos)
            # end = space_pos if space_pos > 0 else header_size
            end = pos
            while end < header_size:
                if header[end] == SPACE:
                    break
                end += 1

            if flag == INT_FLAG_CAS_TOKEN:
                self.cas_token = int(header[pos:end])
            elif flag == INT_FLAG_FETCHED:
                self.fetched = int(header[pos:end])
            elif flag == INT_FLAG_LAST_ACCESS:
                self.last_access = int(header[pos:end])
            elif flag == INT_FLAG_TTL:
                self.ttl = int(header[pos:end])
            elif flag == INT_FLAG_CLIENT_FLAG:
                self.client_flag = int(header[pos:end])
            elif flag == FLAG_WIN:
                self.win = True
            elif flag == FLAG_LOST:
                self.win = False
            elif flag == FLAG_STALE:
                self.stale = True
            elif flag == INT_FLAG_SIZE:
                self.real_size = int(header[pos:end])
            elif flag == TOKEN_FLAG_OPAQUE:
                self.opaque = header[pos:end]
            pos = end + 1


@dataclass(slots=True, init=False)
class Value(Success):
    # __slots__ = ("header", "flag_positions", "size", "value")
    size: int
    value: Optional[Any]

    def __init__(
        self,
        *,
        size: int,
        value: Optional[Any] = None,
        cas_token: Optional[int] = None,
        fetched: Optional[int] = None,
        last_access: Optional[int] = None,
        ttl: Optional[int] = None,
        client_flag: Optional[int] = None,
        win: Optional[bool] = None,
        stale: Optional[bool] = None,
        real_size: Optional[int] = None,
        opaque: Optional[bytes] = None,
    ) -> None:
        self.size = size
        self.value = value
        self.cas_token = cas_token
        self.fetched = fetched
        self.last_access = last_access
        self.ttl = ttl
        self.client_flag = client_flag
        self.win = win
        self.stale = stale
        self.real_size = real_size
        self.opaque = opaque

    @classmethod
    def from_header(cls, header: Blob) -> "Value":
        header_size = len(header)
        if header_size < 4 or header[2] != SPACE:
            raise ValueError(f"Invalid header {header!r}")
        # end = header.find(SPACE, 3)
        # size = int(header[3:end])
        end = 4
        while end < header_size:
            if header[end] == SPACE:
                break
            end += 1
        # # end = header_size
        # # for i in range(4, header_size):
        # #     if header[i] == SPACE:
        # #         end = i
        # #         break
        size = int(header[3:end])
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        ############################
        result = cls(size=size)
        result._set_flags(header, pos=end + 1)
        return result


DEFAULT_VALUE = Value(size=0)
#     if header_size >= 4 and header[2] == SPACE:
#         end = header_size
#         for i in range(4, header_size):
#             if header[i] == SPACE:
#                 end = i
#                 break
#         size = int(header[3:end])
#         return size, _get_flag_positions(header, pos=end + 1)
#     raise ValueError(f"Invalid header {header!r}")

# def __init__(self, header: Blob) -> None:
#     self.header = header
#     self.flag_positions = _get_flag_positions(header)

# def flag(self, flag: Flag) -> bool:
#     flag_value = flag.value[0]
#     for pos in self.flag_positions:
#         if self.header[pos] == flag_value:
#             return True
#     return False

# @overload
# def int_flag(self, flag: IntFlag) -> Optional[int]:
#     ...

# @overload
# def int_flag(self, flag: IntFlag, default: None) -> Optional[int]:
#     ...

# @overload
# def int_flag(self, flag: IntFlag, default: int) -> int:
#     ...

# def int_flag(self, flag: IntFlag, default: Optional[int] = None) -> Optional[int]:
#     flag_value = flag.value[0]
#     value = self._value_flag(flag_value)
#     return int(value) if value is not None else default

# @overload
# def token_flag(self, flag: TokenFlag) -> Optional[bytes]:
#     ...

# @overload
# def token_flag(self, flag: TokenFlag, default: None) -> Optional[bytes]:
#     ...

# @overload
# def token_flag(self, flag: TokenFlag, default: bytes) -> bytes:
#     ...

# def token_flag(
#     self, flag: TokenFlag, default: Optional[bytes] = None
# ) -> Optional[bytes]:
#     flag_value = flag.value[0]
#     value = self._value_flag(flag_value)
#     return value if value is not None else default

# def _value_flag(self, flag: int) -> Optional[bytes]:
#     for i, pos in enumerate(self.flag_positions):
#         if self.header[pos] == flag:
#             start = pos + 1
#             next_flag = i + 1
#             end = (
#                 self.flag_positions[next_flag] - 1
#                 if next_flag < len(self.flag_positions)
#                 else len(self.header)
#             )
#             return self.header[start:end]
#     return None


# class Value(Success):
#     __slots__ = ("header", "flag_positions", "size", "value")
#     size: int
#     value: Optional[Any]

#     def __init__(
#         self,
#         header: Blob,
#         value: Optional[Any] = None,
#     ) -> None:
#         self.header = header
#         self.size, self.flag_positions = _get_size_and_flag_positions(header)
#         self.value = value


@dataclass
class NotStored(MemcacheResponse):
    __slots__ = ()


@dataclass
class Conflict(MemcacheResponse):
    __slots__ = ()


ReadResponse = Union[Miss, Value, Success]
WriteResponse = Union[Success, NotStored, Conflict, Miss]


@dataclass(slots=True)
class ValueContainer:
    value: Any


MaybeValue = Optional[ValueContainer]
MaybeValues = Optional[List[ValueContainer]]


class ServerVersion(IntEnum):
    """
    If more versions with breaking changes are
    added, bump stable to the next int. Code
    will be able to use > / < / = to code
    the behavior of the different versions.
    """

    AWS_1_6_6 = 1
    STABLE = 2


def get_store_success_response_header(version: ServerVersion) -> bytes:
    if version == ServerVersion.AWS_1_6_6:
        return b"OK"
    return b"HD"


def encode_size(size: int, version: ServerVersion) -> bytes:
    if version == ServerVersion.AWS_1_6_6:
        return b"S" + str(size).encode("ascii")
    else:
        return str(size).encode("ascii")
