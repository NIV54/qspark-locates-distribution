import json
import math
from itertools import groupby
from operator import itemgetter
from typing import List

from constants import FULL_LOCATE_SIZE
from dummy_data import case1
from external_api import request_locates
from models import AggregatedLocatesRequest, LocateDistribution


def append_missing_symbols(locates_request: AggregatedLocatesRequest, locates_received: AggregatedLocatesRequest) -> AggregatedLocatesRequest:
    for key, value in locates_request.items():
        if key not in locates_received:
            locates_received[key] = 0
    return locates_received


def round_down_to_full_locate(locates: int | float):
    return int(math.floor(locates / FULL_LOCATE_SIZE)) * FULL_LOCATE_SIZE


def sort_by_highest_partial_locate_first(locate_distributions: List[LocateDistribution]) -> List[LocateDistribution]:
    return sorted(
        locate_distributions,
        key=lambda x: x['number_of_locates_given'] % FULL_LOCATE_SIZE,
        reverse=True
    )


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
    locates_received = append_missing_symbols(
        locates_request, locates_received)
    print("Locates received: ", json.dumps(locates_received, indent=2))
    locate_distributions: List[LocateDistribution] = []
    for key, value in locates_received.items():
        # all fulfilled
        if locates_request[key] <= value:
            for current_request in requests_by_symbol[key]:
                locate_distributions.append({
                    **current_request,
                    'number_of_locates_given': current_request['number_of_locates_requested']
                })
            continue

        # partial fulfillment
        # starting with "fair" split
        current_distributions: List[LocateDistribution] = []
        for current_request in requests_by_symbol[key]:
            current_distributions.append({
                **current_request,
                'number_of_locates_given': (current_request['number_of_locates_requested'] / locates_request[key]) * value
            })

        partial_locates_sum = sum(map(
            lambda x: x['number_of_locates_given'] % FULL_LOCATE_SIZE,
            current_distributions
        ))

        # giving out a full locate to whoever possible, and rounding down the rest
        for current_distribution in sort_by_highest_partial_locate_first(current_distributions):
            current_distribution['number_of_locates_given'] = round_down_to_full_locate(
                current_distribution['number_of_locates_given'])
            if partial_locates_sum >= FULL_LOCATE_SIZE:
                current_distribution['number_of_locates_given'] = FULL_LOCATE_SIZE
                partial_locates_sum -= FULL_LOCATE_SIZE
            else:
                current_distribution['number_of_locates_given'] += partial_locates_sum
                partial_locates_sum = 0

        locate_distributions.extend(current_distributions)

    print("Locates given: ", json.dumps(locate_distributions, indent=2))


if __name__ == "__main__":
    main()
