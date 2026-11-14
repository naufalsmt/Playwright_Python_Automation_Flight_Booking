import pytest

from pages.flight_results_page import FlightResultsPage

@pytest.mark.parametrize(
    'multiple_flight_search, expected_section',
    [
        (('London', 'Dubai'), 2),
        (('Dubai', 'London'), 2),
        (('London', 'Tokyo'), 2)
    ],
    indirect = ['multiple_flight_search']
)
def test_flight_result_section_count(multiple_flight_search, expected_section):
    flight_result = FlightResultsPage(multiple_flight_search)
    actual_count = flight_result.get_section_count()
    # print(f"\n\nActual count: {actual_count}")
    # print(f"Expected count: {expected_section}")
    assert actual_count == expected_section

@pytest.mark.parametrize(
    'multiple_flight_search, expected_route',
    [
        (('Dubai', 'London'), "Dubai → London"),
        (('London', 'Dubai'), "London → Dubai"),
        (('Dubai', 'Tokyo'),  "Dubai → Tokyo")
    ],
    indirect = ['multiple_flight_search']
)
def test_search_flight_routes(multiple_flight_search, expected_route):
    flight_result = FlightResultsPage(multiple_flight_search)
    actual_route = flight_result.get_first_departure_route()
    # print(f"\n\nActual rout: {actual_route}")
    # print(f"Expected rout: {expected_route}")
    assert actual_route == expected_route