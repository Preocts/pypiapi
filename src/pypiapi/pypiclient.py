"""Offer two methods to GET package data from PyPI"""
from __future__ import annotations

import json
import logging
from typing import Any

import httpx
from pypiapi.models.project import Project


class PyPIClient:
    """Offer two methods to GET package data from PyPI"""

    log = logging.getLogger(__name__)

    def get_project(self, project_name: str) -> Project | None:
        """Return, if found, the most recent project version metadata"""
        url = f"https://pypi.org/pypi/{project_name}/json"
        response = httpx.get(url)
        return self._process_result(response)

    def get_project_by_version(
        self,
        project_name: str,
        version: str,
    ) -> Project | None:
        """Return, if found, the provided project version metadata"""
        url = f"https://pypi.org/pypi/{project_name}/{version}/json"
        response = httpx.get(url)
        return self._process_result(response)

    def _process_result(self, response: httpx.Response) -> Project | None:
        """Internal: Handle responses"""
        result: dict[str, Any] = {}
        try:
            result = response.json()
        except json.JSONDecodeError:
            self.log.error("Error: [%s] %s", response.status_code, response.text)
        return Project.from_dict(result) if result else None
