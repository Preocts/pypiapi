"""
Test the health of our model
"""
import json
from dataclasses import is_dataclass
from typing import Any
from typing import Dict

import pytest
from pypiapi.models.project import Project

Payload = Dict[str, Any]


@pytest.fixture(scope="function", name="payload")
def fixture_payload() -> Payload:
    """Ensure fixture is not polluted"""
    with open("tests/fixtures/json_response.json", "r", encoding="utf-8") as fixture:
        return json.load(fixture)["json"]


def test_load_with_provided_example(payload: Payload) -> None:
    """Provided example should match our model, but is likely less than our model"""
    project = Project.from_dict(payload)

    assert is_dataclass(project)
    assert is_dataclass(project.info)
    for url in project.urls:
        assert is_dataclass(url)
    for release in project.releases.values():
        for subrelease in release:
            assert is_dataclass(subrelease)


def test_load_with_missing_subvalues(payload: Payload) -> None:
    """Remove nested values to ensure curator loads"""
    payload["info"]["project_urls"] = {}

    project = Project.from_dict(payload)

    assert is_dataclass(project.info.project_urls)
