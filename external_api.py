import math
import random

from constants import LOCATE_VARIANCE, SYMBOL_VARIANCE
from models import AggregatedLocatesRequest


# simulate external api call
def request_locates(requested_locates: AggregatedLocatesRequest) -> AggregatedLocatesRequest:
    return {
        key: random.randint(math.floor(value * (1 - LOCATE_VARIANCE)),
                            math.floor(value * (1 + LOCATE_VARIANCE)))
        for key, value
        in [x for x in requested_locates.items() if random.random() >= SYMBOL_VARIANCE]
    }
