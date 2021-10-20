from dataclasses import dataclass
from typing import Any
from typing import Dict
from typing import List

from pypiapi.models.info import Downloads
from pypiapi.models.info import Info
from pypiapi.models.info import ProjectUrls
from pypiapi.models.release import Digests
from pypiapi.models.release import Release


@dataclass
class Project:
    info: Info
    last_serial: int
    releases: Dict[str, List[Release]]
    urls: List[Release]
    vulnerabilities: List[str]

    @classmethod
    def from_dict(cls, api_data: Dict[str, Any]) -> "Project":
        """Create from dict results of API"""
        data = api_data.copy()

        data["info"] = Project._build_info(data["info"])
        data["urls"] = Project._build_urls(data["urls"])
        data["releases"] = Project._build_release(data["releases"])

        return cls(**data)

    @staticmethod
    def _build_urls(data: Dict[str, Any]) -> List[Release]:
        """Build subclass of urls"""
        return [Release(**url) for url in data]

    @staticmethod
    def _build_release(data: Dict[str, Any]) -> Dict[str, List[Release]]:
        """Build subclass of releases"""
        releases: Dict[str, List[Release]] = {}
        for key, value in data.items():
            # Assemble sub-class Digests
            releases[key] = []
            for rdata in value:
                rdata["digests"] = Digests(**rdata["digests"])
                releases[key].append(Release(**rdata))
        return releases

    @staticmethod
    def _build_info(data: Dict[str, Any]) -> Info:
        """Build subclass of info"""
        data["downloads"] = Downloads(**data["downloads"])
        data["project_urls"] = ProjectUrls(**data["project_urls"])
        return Info(**data)
