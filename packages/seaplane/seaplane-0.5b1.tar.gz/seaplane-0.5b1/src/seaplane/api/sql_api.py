from typing import List, NamedTuple

import requests

from seaplane.config import config

from .api_http import headers
from .api_request import method_with_token


class CreatedDatabase(NamedTuple):
    """
    Created database.
    """

    name: str
    username: str
    password: str


class GlobalSQL:
    """
    Class for handle Global SQL API calls.
    """

    def __init__(self) -> None:
        pass

    @method_with_token
    def create_database(self, token: str) -> CreatedDatabase:
        """Create a new Global Seaplane Database.

        Returns
        -------
        CreatedDatabase
            Returns a CreatedDatabase if successful or it will raise an HTTPError otherwise.
        """

        url = f"{config.global_sql_endpoint}/databases"
        resp = requests.post(url, data="{}", headers=headers(token))
        resp.raise_for_status()
        payload = resp.json()
        return CreatedDatabase(
            name=payload["database"],
            username=payload["username"],
            password=payload["password"],
        )

    @method_with_token
    def list_databases(self, token: str) -> List[str]:
        """List all Global Seaplane Databases.

        Returns
        -------
        list[database_name: str]
            Returns a list of database names if successful or it will raise an HTTPError otherwise.
        """
        url = f"{config.global_sql_endpoint}/databases"
        resp = requests.get(url, data="{}", headers=headers(token))
        resp.raise_for_status()
        payload = resp.json()
        return [database["database"] for database in payload["databases"]]
