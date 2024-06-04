from models import AggregatedLocatesRequest


# simulate external api call
def request_locates(requested_locates: AggregatedLocatesRequest) -> AggregatedLocatesRequest:
    return {key: 435 for key, value in requested_locates.items()}
