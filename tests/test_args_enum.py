
import pytest
from pathlib import Path
from args_enum import __version__, Parser, Log, Flag

def test_version():
    assert __version__ == '0.1.0'

def test_logger_conf():
    Args = (
        AppParser := Parser(Log,
        QUIET = Flag.TRUE("log level 'WARNING'"),
        DEBUG = Flag.TRUE("log level 'DEBUG'")
    )
    ).parse_args(["--log-dir", "~/logs", "--debug"])
    assert Args.LOG_DIR == Path("~/logs")
    assert Args.DEBUG == True
    assert isinstance(Args.DEBUG, bool)