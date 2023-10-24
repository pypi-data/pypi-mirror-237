"""Main module for the `sommer` library."""

import dataclasses
import http.client
import json


def entity(cls):
    """Sommer decorator to wrap an entity."""

    class BaseEntity(dataclasses.dataclass(cls)):
        """Base class to define a new entity."""

        def __post_init__(self):
            """Calls Sommer to create row."""
            table_name = cls.__name__
            rows = [dataclasses.asdict(self)]
            payload = json.dumps({"table_name": table_name, "rows": rows})
            connection = http.client.HTTPConnection("localhost:8600")
            headers = {
                "Content-Type": "application/json",
                "Content-Length": len(payload),
            }
            connection.request("POST", "/row/new", payload, headers)
            connection.getresponse()

    return dataclasses.dataclass(BaseEntity)
