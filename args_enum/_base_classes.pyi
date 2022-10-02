from enum import Enum
from pathlib import Path
from argparse import ArgumentParser
from typing import Annotated, Any, Collection, Iterable, Literal, Optional, Type, TypeAlias, TypedDict, Union

_ATYP: TypeAlias = Union[int, float, str, Path]
_PTYP: TypeAlias = Union[str, None]
Group: TypeAlias = Enum

class _ActionArgs(TypedDict):
    default:    _ATYP
    type:       _ATYP

class _ParserArgs(TypedDict):
    usage:              _PTYP
    description:        _PTYP
    epilog:             _PTYP
    parents:            Iterable[ArgumentParser]
    argument_default:   Any
    conflict_handler:   str
    add_help:           bool
    exit_on_error:      bool

class _AEdict(TypedDict):
    name: str
    group: str
    dest: str

class Actions(Annotated[dict, Enum]):
    
    action: Annotated[str, property]
    opt: Annotated[str, property]
    ingroup_opt: Annotated[str, property]

    @staticmethod
    def fmt(fstr) -> str: ...
    @property
    def __dict__(self) -> _AEdict: ...

    def __new__(cls,
        __v: _ActionArgs
    ) -> _ActionArgs: ...

    def __init__(self,
        action: Literal['store', 'store_const', 'store_true', 'store_false'],
        default: Optional[Any],
        type: Optional[Type]
    ) -> None: ...

    def __call__(self,
        default: Optional[Any],
        choices: Optional[Collection[Any]],
        const: Optional[Any]
    ) -> _ActionArgs: ...

class Parser(ArgumentParser):

    def init_group(self,
        arg_group: Type[Actions],
        **kwargs
    ) -> ArgumentParser: ...

    def __init__(self,
        *subparsers: Type[Actions]
    ) -> None: ...
