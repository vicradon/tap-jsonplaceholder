"""jsonplaceholder tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_jsonplaceholder.streams import (
    jsonplaceholderStream,
    UsersStream,
    GroupsStream,
    CommentsStream
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    CommentsStream
]


class Tapjsonplaceholder(Tap):
    """jsonplaceholder tap class."""
    name = "tap-jsonplaceholder"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        # th.Property(
        #     "auth_token",
        #     th.StringType,
        #     required=False,
        #     description="The token to authenticate against the API service"
        # ),
        # th.Property(
        #     "project_ids",
        #     th.ArrayType(th.StringType),
        #     required=True,
        #     description="Project IDs to replicate"
        # ),
        # th.Property(
        #     "start_date",
        #     th.DateTimeType,
        #     description="The earliest record date to sync"
        # ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://jsonplaceholder.typicode.com",
            description="The json placeholder API"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
