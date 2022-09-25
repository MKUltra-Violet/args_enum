from ctypes import Union
from enum import Enum
from pathlib import Path
from argparse import ArgumentParser, Namespace
from typing import Annotated, Callable, TypedDict, Union

class _CallArgs(TypedDict):
    default: int
    type: Union[int, float, str, Path]

class _Arg(dict, Enum):
    action: Annotated[property, str]
    __new__: Callable[[dict], Annotated[Enum, _CallArgs]]

    def __init__(self, __v) -> None:
        self._value_ = __v | \
        dict(
            action = self.action.lower(),
        )
    def __call__(self, **kwargs: _CallArgs) -> dict:
        return self.value | kwargs

class Store(_Arg):
    @property
    def action(self): return 'store'
    STRING = {}
    INT = {'type': int}
    PATH = {'type': Path}

class Flag(_Arg):
    @property
    def action(self): return f'store_{self.name}'

    TRUE = {}
    FALSE = {}

class Args(Enum):

    @classmethod
    def parse_args(cls) -> Namespace:
        parser = ArgumentParser()
        for arg in cls._member_map_.values():
            parser.add_argument(
                f"--{arg.name}".lower(),
                dest = arg.name,
                **arg.value)
        args: cls = parser.parse_args()
        return args