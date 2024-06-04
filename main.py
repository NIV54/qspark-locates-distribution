import json
from itertools import groupby
from operator import itemgetter
from typing import List

from dummy_data import case1
from models import AggregatedLocatesRequest, LocateDistribution, LocateRequest


def request_locates(requested_locates: AggregatedLocatesRequest) -> AggregatedLocatesRequest:
    return {key: 500 for key, value in requested_locates.items()}


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

    locate_distributions: List[LocateDistribution] = []
    for key, value in locates_received.items():
        # all fulfilled
        if locates_request[key] <= value:
            for single_request in requests_by_symbol[key]:
                locate_distributions.append({
                    **single_request,
                    'number_of_locates_given': single_request['number_of_locates_requested']
                })
            continue

        # partial fulfillment
        for single_request in requests_by_symbol[key]:
            locate_distributions.append({
                **single_request,
                'number_of_locates_given': (single_request['number_of_locates_requested'] / locates_request[key]) * value
            })

    print(json.dumps(locate_distributions, indent=2))


if __name__ == "__main__":
    main()
