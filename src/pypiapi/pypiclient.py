"""Offer two methods to GET package data from PyPI"""
import json
import logging
from typing import Any
from typing import Dict
from typing import Optional

from pypiapi import util_http as _util_http
from pypiapi.models.project import Project


class PyPIClient:
    """Offer two methods to GET package data from PyPI"""

    log = logging.getLogger(__name__)
    http = _util_http.get_connection()

    def get_project(self, project_name: str) -> Optional[Project]:
        """Return, if found, the most recent project version metadata"""
        url = f"https://pypi.org/pypi/{project_name}/json"
        response = self.http.request("GET", url)
        return self._process_result(response)

    def get_project_by_version(
        self,
        project_name: str,
        version: str,
    ) -> Optional[Project]:
        """Return, if found, the most recent project version metadata"""
        url = f"https://pypi.org/pypi/{project_name}/{version}/json"
        response = self.http.request("GET", url)
        return self._process_result(response)

    def _process_result(self, response: Any) -> Optional[Project]:
        """Internal: Handle responses"""
        result = self._jsonify(response.data)
        if "error" in result:
            self.log.error("Error: %s", result)
        return Project.from_dict(result) if "error" not in result else None

    @staticmethod
    def _jsonify(data: bytes) -> Dict[str, Any]:
        """Translate response bytes to dict, returns key 'error' if failed"""
        try:
            return json.loads(data.decode("utf-8"))
        except json.JSONDecodeError:
            return {"error": data}
