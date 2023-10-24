import datetime
from typing import Any, Dict, List, Optional, TypedDict

import requests
from seaplane_framework.api.apis.tags import object_api
from seaplane_framework.api.model.bucket import Bucket

from .api.api_http import headers
from .api.api_request import get_pdk_client, method_with_token
from .config import config

SP_BUCKETS = ["seaplane-internal-flows"]


# A little copy paste is better than a little dependency.
def _sizeof_fmt(num: float, suffix: str = "B") -> str:
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


class ListObjectsMetadata(TypedDict):
    """
    Dictionary wrapping the metadata returned by the `list_objects()` endpoint.
    """

    name: str
    digest: str
    created_at: datetime.datetime
    size: str


class ObjectStorageAPI:
    """
    Class for handle Object Storage API calls.
    """

    def __init__(self) -> None:
        pass

    def get_object_api(self, access_token: str) -> object_api.ObjectApi:
        return object_api.ObjectApi(get_pdk_client(access_token))

    @method_with_token
    def list_buckets(self, token: str) -> List[str]:
        api = self.get_object_api(token)
        list = []
        resp = api.list_buckets()
        for name, _ in sorted(resp.body.items()):
            if name not in SP_BUCKETS:
                list.append(name)

        return list

    @method_with_token
    def create_bucket(self, token: str, name: str, body: Optional[Bucket] = None) -> bool:
        if name in SP_BUCKETS:
            return False

        if not body:
            body = {}

        api = self.get_object_api(token)
        path_params = {
            "bucket_name": name,
        }
        api.create_bucket(
            path_params=path_params,
            body=body,
        )
        return True

    @method_with_token
    def delete_bucket(self, token: str, name: str) -> bool:
        if name in SP_BUCKETS:
            return False
        api = self.get_object_api(token)
        path_params = {
            "bucket_name": name,
        }
        api.delete_bucket(path_params=path_params)
        return True

    def exists(self, bucket: str, object: str) -> bool:
        raise Exception("TODO")

    @method_with_token
    def list_objects(
        self, token: str, bucket_name: str, path_prefix: str
    ) -> List[ListObjectsMetadata]:
        api = self.get_object_api(token)

        path_params = {
            "bucket_name": bucket_name,
        }
        query_params = {
            "path": path_prefix,
        }
        resp = api.list_objects(
            path_params=path_params,
            query_params=query_params,
        )

        table = [
            ListObjectsMetadata(
                name=x["name"],
                digest=x["digest"],
                created_at=datetime.datetime.fromtimestamp(int(x["mod_time"])),
                size=_sizeof_fmt(int(x["size"])),
            )
            for x in resp.body
        ]

        return table

    @method_with_token
    def download(self, token: str, bucket_name: str, path: str) -> bytes:
        url = f"{config.carrier_endpoint}/object/{bucket_name}/store"

        params: Dict[str, Any] = {}
        params["path"] = path
        resp = requests.get(
            url,
            params=params,
            headers=headers(token, "application/octet-stream"),
        )
        return resp.content

    def file_url(self, bucket_name: str, path: str) -> str:
        """
        Builds a URL usable to download the object stored at the given bucket & path.
        """
        return f"{config.carrier_endpoint}/object/{bucket_name}/store?path={path}"

    @method_with_token
    def upload(self, token: str, bucket_name: str, path: str, object: bytes) -> bool:
        if bucket_name in SP_BUCKETS:
            return False
        api = self.get_object_api(token)

        path_params = {
            "bucket_name": bucket_name,
        }
        query_params = {
            "path": path,
        }

        api.create_object(
            path_params=path_params,
            query_params=query_params,
            body=object,
        )

        return True

    def upload_file(self, bucket_name: str, path: str, object_path: str) -> bool:
        if bucket_name in SP_BUCKETS:
            return False
        with open(object_path, "rb") as file:
            file_data = file.read()

        return self.upload(bucket_name, path, file_data)

    @method_with_token
    def delete(self, token: str, bucket_name: str, path: str) -> Any:
        if bucket_name in SP_BUCKETS:
            return False
        api = self.get_object_api(token)
        path_params = {
            "bucket_name": bucket_name,
        }
        query_params = {
            "path": path,
        }
        api.delete_object(
            path_params=path_params,
            query_params=query_params,
        )
        return True


object_store = ObjectStorageAPI()
