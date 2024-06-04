from typing import List

from models import LocateRequest

case1: List[LocateRequest] = [
    {'client_name': 'Client1', 'symbol': 'ABC',
        'number_of_locates_requested': 300},
    {'client_name': 'Client2', 'symbol': 'ABC',
        'number_of_locates_requested': 200},
    {'client_name': 'Client3', 'symbol': 'ABC',
        'number_of_locates_requested': 100},
    {'client_name': 'Client1', 'symbol': 'EGF',
        'number_of_locates_requested': 400},
    {'client_name': 'Client2', 'symbol': 'EGF',
        'number_of_locates_requested': 300},
    {'client_name': 'Client3', 'symbol': 'EGF',
        'number_of_locates_requested': 100},
]
