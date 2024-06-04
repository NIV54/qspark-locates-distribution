from itertools import groupby
from operator import itemgetter
from typing import List

from dummy_data import case1
from models import AggregatedLocatesRequest, LocateRequest


def request_locates(requested_locates: AggregatedLocatesRequest) -> AggregatedLocatesRequest:
    return {key: 600 for key, value in requested_locates.items()}


def main():
    requests_by_symbol = {
        key: [item for item in group]
        for key, group in groupby(case1, itemgetter('symbol'))
    }

    locates_request: AggregatedLocatesRequest = {
        key: sum(map(
            itemgetter('number_of_locates_requested'),
            group
        ))
        for key, group in requests_by_symbol.items()
    }

    locates_received = request_locates(locates_request)

    result: List[LocateRequest] = []
    for key, value in locates_received.items():
        if locates_request[key] <= value:
            for single_request in requests_by_symbol[key]:
                result.append({
                    'client_name': single_request['client_name'],
                    'symbol': single_request['symbol'],
                    'number_of_locates_requested': single_request['number_of_locates_requested']
                })

    print(result)


if __name__ == "__main__":
    main()
