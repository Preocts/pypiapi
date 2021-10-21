import logging
from dataclasses import fields
from dataclasses import is_dataclass
from dataclasses import MISSING
from typing import Any
from typing import Dict
from typing import Type

__all__ = ["curator"]

log = logging.getLogger(__name__)


def curator(
    dataclass: Type[Any],
    dict_in: Dict[str, Any],
    *,
    add_missing: bool = True,
    default_value: Any = None,
    remove_extra: bool = True,
    log_actions: bool = False,
) -> Dict[str, Any]:
    """
    Accepts any dataclass and dict. Returns a dict that will unpack into dataclass

    This is done by matching the dataclass attributes with the
    dictionary's keys. Missing key/ values, by default, are added
    as `None`. Extra values are dropped.

    Does not enforce type-hints. Does not override attribute defaults.
    """
    log.setLevel(level="DEBUG" if log_actions else "CRITICAL")

    if not is_dataclass(dataclass):
        log.error("Provided dataclass is not a dataclasses.dataclass")
        raise TypeError("Expected Dataclass")

    return_dict = dict_in.copy()
    # List all attributes of dataclass
    names = [f.name for f in fields(dataclass) if f.default is MISSING]
    # Track which have defaults, do not delete
    defaults = [f.name for f in fields(dataclass) if f.default is not MISSING]

    if add_missing:
        update = {name: default_value for name in names if name not in dict_in.keys()}
        log.info("Adding key/values to provided data: %s", update)
        return_dict.update(update)

    if remove_extra:
        remove = [key for key in dict_in.keys() if key not in names]
        for key in remove:
            if key not in defaults:
                log.info("Removing unused key: `%s`", key)
                return_dict.pop(key)

    return return_dict
