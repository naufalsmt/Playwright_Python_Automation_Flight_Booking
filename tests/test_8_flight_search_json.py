import pytest

from pages.flight_results_page import FlightResultsPage
from utils.json_reader import read_json, validate_json_data

flight_data = read_json('flight_test_data.json')
# flight_data = read_json('flight_test1_data.json')
# flight_data = read_json('invalid_json.json')


@pytest.mark.parametrize(
    'multiple_flight_search, expected_route',
    [
        (
            (data['departure'], data['destination']),
            data['expected_route']
        )
        for data in flight_data
    ],
    indirect = ['multiple_flight_search']
)
def test_flight_search_from_json(multiple_flight_search, expected_route):
    flight_result = FlightResultsPage(multiple_flight_search)
    actual_route = flight_result.get_first_departure_route()
    assert actual_route == expected_route
    print(f'\n\nPASS: Flight route correctly verified with respect to search route {actual_route}')


def test_flight_data_json(flight_test_data):
    validate_json_data(flight_test_data)
    print('PASS: All three values are present in Json')
    print('PASS: All three values should not be empty')


def test_invalid_flight_json():

    invalid_data = [
        {
            "departure": "",
            "destination": "London",
            "expected_route": "Dubai → London"
        }
    ]

    with pytest.raises(AssertionError):
        validate_json_data(invalid_data)
    print('PASS: Assertion error validated for invalid json')


@pytest.mark.parametrize(
    "invalid_data, expected_error",
    [
        ([
            {
                "departure": "",
                "destination": "London",
                "expected_route": "Dubai → London"
            }
        ], 'Departure value is empty'),
        ([
            {
                "departure": "Dubai",
                "destination": "",
                "expected_route": "Dubai → London"
            }
        ], 'Destination value is empty'),
        ([
            {
                "departure": "Dubai",
                "destination": "London",
                "expected_route": ""
            }
        ], 'Expected route value is empty')
    ]
)
def test_invalid_flight_json_parameterized(invalid_data, expected_error):
    with pytest.raises(AssertionError, match=expected_error):
        validate_json_data(invalid_data)

    print('PASS: Validation message correctly printed successfully')