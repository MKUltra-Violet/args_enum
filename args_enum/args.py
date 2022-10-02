from pathlib import Path
from ._base_classes import Group, Actions

class Store(Actions):

    action = Actions.fmt('store')

    STRING = {}
    INT    = {'type': int}
    PATH   = {'type': Path}

class Flag(Actions):
    action = Actions.fmt('store_{name}')

    TRUE  = {}
    FALSE = {}

class Log(Group):
    LEVEL = Store.STRING(
        "Sets log message verbosity",
        default = "WARNING",
        choices = ["NOTSET", "TRACE", "DEBUG", "INFO", "WARNING"]
    )
    DIR: Path = Store.PATH(
        "Destination directory for log files",
        default = "~/logs"
    )