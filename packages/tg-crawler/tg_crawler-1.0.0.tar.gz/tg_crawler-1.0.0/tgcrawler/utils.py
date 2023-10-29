import os
import sys
import subprocess
from datetime import datetime
from termcolor import colored

START_TIME = datetime.utcnow()


def progress_bar(
    current: int,
    total: int,
    char="█",
    desc=None,
    ncols=75,
    unit="it",
    unit_scale=False,
    unit_divisor=1000,
    color="cyan",
):
    filled_length = int(ncols * current // total)
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    _desc = f"{desc}:   " if desc else ""
    bar = colored(char * filled_length + " " * (ncols - filled_length), color)
    percentage = current / total * 100
    if unit_scale:
        csl, ucsl = unit_from_bytes(current, int(unit_divisor))
        tsl, utsl = unit_from_bytes(total, int(unit_divisor))
    elif not unit_scale:
        csl, ucsl = current, unit[0] if isinstance(unit, list) else unit
        tsl, utsl = total, unit[1] if isinstance(unit, list) else unit
    print(
        f"\r{_desc}{percentage:.1f}%|{bar}| {round(csl)}{ucsl}/{tsl}{utsl} in [{_execution_time(uptime_sec)}]",
        end="",
        flush=True,
    )


def opener(path):
    if sys.platform == "win32":
        os.startfile(path)
    else:
        _opener_ = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([_opener_, path])


def unit_from_bytes(byte_count, divisor):
    """Get unit from a byte count (in KB, MB...)"""
    suffix_index = 0
    while byte_count >= divisor:
        byte_count /= divisor
        suffix_index += 1

    return round(byte_count, 2), ["bytes", "KB", "MB", "GB", "TB"][suffix_index]


_TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


def _execution_time(seconds: int):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in _TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{:02d}".format(amount))
    return ":".join(parts)
