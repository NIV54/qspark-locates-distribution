from typing import TypedDict

AggregatedLocatesRequest = dict[str, int]


class LocateRequest(TypedDict):
    client_name: str
    symbol: str
    number_of_locates_requested: int
