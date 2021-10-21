import dataclasses
from typing import List
from typing import Optional


@dataclasses.dataclass
class ProjectUrls:
    Download: Optional[str] = ""
    Homepage: Optional[str] = ""


@dataclasses.dataclass
class Downloads:
    last_day: int = -1
    last_month: int = -1
    last_week: int = -1


@dataclasses.dataclass
class Info:
    author: str = ""
    author_email: str = ""
    bugtrack_url: str = ""
    classifiers: List[str] = dataclasses.field(default_factory=list)
    description: str = ""
    description_content_type: Optional[str] = None
    docs_url: Optional[str] = None
    download_url: str = ""
    downloads: Downloads = Downloads()
    home_page: str = ""
    keywords: str = ""
    license: str = ""
    maintainer: Optional[str] = None
    maintainer_email: Optional[str] = None
    name: str = ""
    package_url: str = ""
    platform: str = ""
    project_url: str = ""
    project_urls: ProjectUrls = ProjectUrls()
    release_url: str = ""
    requires_dist: Optional[str] = None
    requires_python: Optional[str] = None
    summary: str = ""
    version: str = ""
    yanked: bool = False
    yanked_reason: Optional[str] = ""
