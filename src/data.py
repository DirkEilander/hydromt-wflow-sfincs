import os
import shutil
from os.path import dirname, isdir
from urllib.parse import urlparse

import requests


def _uri_validator(uri: str) -> bool:
    """Check if uri is valid"""
    try:
        result = urlparse(uri)
        return all([result.scheme, result.netloc])
    except:
        return False
    
def copyfile(src, dst):
    """Copy src file to dst. This method supports both online and local files."""
    if not isdir(dirname(dst)):
        os.makedirs(dirname(dst))
    if _uri_validator(str(src)):
        with requests.get(src, stream=True) as r:
            if r.status_code != 200:
                raise ConnectionError(
                    f"Data download failed with status code {r.status_code}"
                )
            with open(dst, "wb") as f:
                shutil.copyfileobj(r.raw, f)
    else:
        shutil.copyfile(src, dst)

