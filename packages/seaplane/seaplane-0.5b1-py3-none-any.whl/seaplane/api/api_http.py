from importlib.metadata import version
import json
from typing import Any, Dict, NamedTuple, Optional

SDK_HTTP_ERROR_CODE = 0


def headers(api_key: Optional[str], content_type: str = "application/json") -> Dict[str, str]:

    return {
        "Accept": "application/json",
        "Content-Type": content_type,
        "Authorization": f"Bearer {api_key}",
        "X-Seaplane-Sdk-Version": version("seaplane"),
    }


def to_json(any: NamedTuple) -> Any:
    return json.loads(json.dumps(any), object_hook=_remove_nulls)


def _remove_nulls(d: Dict[Any, Any]) -> Dict[Any, Any]:
    return {k: v for k, v in d.items() if v is not None}
