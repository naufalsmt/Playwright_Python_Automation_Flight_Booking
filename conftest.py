import pytest
from playwright.sync_api import sync_playwright
from pages.flight_search_page import FlightSearchPage

from utils.json_reader import read_json

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=['--start-maximized']
        )
        context = browser.new_context(
            no_viewport=True
        )
        page = context.new_page()

        yield page
        browser.close()


@pytest.fixture
def search_flight(page):
    flight_search = FlightSearchPage(page)

    flight_search.navigate()

    flight_search.select_flight_from('Dubai')
    flight_search.select_flight_to('London')
    flight_search.enter_departure_date('2026-11-13')
    flight_search.enter_return_date('2026-12-13')
    flight_search.enter_passenger_count(2)
    flight_search.select_flight_class('Business')

    flight_search.check_one_way()
    flight_search.uncheck_one_way()

    flight_search.click_search_flight()

    return page


@pytest.fixture
def multiple_flight_search(page, request):
    departure, destination = request.param
    flight_search = FlightSearchPage(page)

    flight_search.navigate()

    flight_search.select_flight_from(departure)
    flight_search.select_flight_to(destination)
    flight_search.enter_departure_date('2026-11-13')
    flight_search.enter_return_date('2026-12-13')
    flight_search.enter_passenger_count(2)
    flight_search.select_flight_class('Business')

    flight_search.check_one_way()
    flight_search.uncheck_one_way()

    flight_search.click_search_flight()

    return page


@pytest.fixture(scope="session")
def flight_test_data():
    return read_json('flight_test_data.json')


@pytest.fixture
def sample_print():
    print('\n\nBefore yield')
    yield
    print('\nAfter yield')
