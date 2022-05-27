from pypiapi import PyPIClient


def test_successful_pull_name_only() -> None:
    client = PyPIClient()
    project = client.get_project("secretbox")
    assert project is not None


def test_failure_pull_name_only() -> None:
    client = PyPIClient()
    project = client.get_project(" invalid name")
    assert project is None


def test_successful_pull_name_and_version() -> None:
    client = PyPIClient()
    project = client.get_project_by_version("secretbox", "1.6.1")
    assert project is not None


def test_failure_pull_name_and_bad_version() -> None:
    client = PyPIClient()
    project = client.get_project_by_version("secretbox", "1.7")
    assert project is None
