"""Parse/format compact durations like 1h30m. Standard library only."""
import re

_UNIT = {"s": 1, "m": 60, "h": 3600, "d": 86400}
_TOKEN = re.compile(r"(\d+)([smhd])")


def parse(text):
    total, matched = 0, False
    for num, unit in _TOKEN.findall(text.strip()):
        total += int(num) * _UNIT[unit]
        matched = True
    if not matched:
        raise ValueError("no duration tokens found")
    return total


def format(seconds):
    out, seconds = [], int(seconds)
    for unit in ("d", "h", "m", "s"):
        q, seconds = divmod(seconds, _UNIT[unit])
        if q:
            out.append(f"{q}{unit}")
    return "".join(out) or "0s"
