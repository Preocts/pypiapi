from dataclasses import dataclass
from typing import Optional


@dataclass
class Digests:
    md5: str = ""
    sha256: str = ""


@dataclass
class Release:
    comment_text: str = ""
    digests: Digests = Digests()
    downloads: int = -1
    filename: str = ""
    has_sig: bool = False
    md5_digest: str = ""
    packagetype: str = ""
    python_version: str = ""
    requires_python: Optional[str] = None
    size: int = 0
    upload_time: str = ""
    upload_time_iso_8601: str = ""
    url: str = ""
    yanked: bool = False
    yanked_reason: Optional[str] = None
