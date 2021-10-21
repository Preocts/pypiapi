import dataclasses

import pytest
from pypiapi.util_curator import curator


@dataclasses.dataclass
class MockClass:
    string: str
    value: int = 5


class NotDataClass:
    string: str
    value: int


SAMPLE_SMALL = {"value": 10}
SAMPLE_MATCH = {"value": 10, "string": "Hello"}
SAMPLE_LARGE = {"value": 10, "string": "Goodbye", "bool": True}
SAMPLE_DEFAULTS = {"nothing": False}


def test_curator_invalid_dataclass() -> None:
    with pytest.raises(TypeError):
        curator(NotDataClass, SAMPLE_MATCH)


def test_curator_respect_default_values() -> None:
    result = MockClass(**curator(MockClass, SAMPLE_DEFAULTS))
    assert result.string is None
    assert result.value == 5


def test_curator_sample_too_small() -> None:
    result = MockClass(**curator(MockClass, SAMPLE_SMALL))
    assert result.string is None
    assert result.value == 10


def test_curator_sample_matches() -> None:
    result = MockClass(**curator(MockClass, SAMPLE_MATCH))
    assert result.string == "Hello"
    assert result.value == 10


def test_curator_sample_too_large() -> None:
    result = MockClass(**curator(MockClass, SAMPLE_LARGE))
    assert result.string == "Goodbye"
    assert result.value == 10


def test_curator_do_not_remove_extra() -> None:
    with pytest.raises(TypeError):
        MockClass(**curator(MockClass, SAMPLE_LARGE, remove_extra=False))


def test_curator_do_not_add_missing() -> None:
    with pytest.raises(TypeError):
        MockClass(**curator(MockClass, SAMPLE_SMALL, add_missing=False))


def test_curator_override_default() -> None:
    result = MockClass(**curator(MockClass, SAMPLE_SMALL, default_value="nope"))
    assert result.string == "nope"
