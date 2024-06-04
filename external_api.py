import math
import random

from models import AggregatedLocatesRequest

# meaning this mock will return 40% less or more of the requested locates
# feel free to change this field if you want
LOCATE_VARIANCE = 0.4

# meaning on 20% of the time this mock will not return a symbol at all,
# mimicking it being out of stock
# feel free to change this field if you want
SYMBOL_VARIANCE = 0.2

# simulate external api call


def request_locates(requested_locates: AggregatedLocatesRequest) -> AggregatedLocatesRequest:
    return {
        key: random.randint(math.floor(value * (1 - LOCATE_VARIANCE)),
                            math.floor(value * (1 + LOCATE_VARIANCE)))
        for key, value
        in [x for x in requested_locates.items() if random.random() >= SYMBOL_VARIANCE]
    }
