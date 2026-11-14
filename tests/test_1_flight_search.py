from playwright.sync_api import expect
from pages.flight_search_page import FlightSearchPage

def test_launch_flight_search_page(page):
    url = 'https://www.qapractice.com/flight-booking-scenarios'
    page.goto(url)
    h1_title = 'Flight Booking Automation Practice'
    assert h1_title in page.locator('h1').inner_text()
    print('\n\nPASS: Browser launched and verified title')

    page_heading = page.locator('h2.section-heading').first
    expect(page_heading).to_be_visible()
    print('PASS: Search page opened and page hading verified successfully')

# use POM pages
def test_launch_flight_search_page_alternative(page):
    flight_search = FlightSearchPage(page)
    flight_search.navigate()
    print('\n\nPASS: Browser launched')
    heading = flight_search.verify_page_heading()
    expect(heading).to_be_visible()
    print('PASS: Search page opened and title verified successfully')

# use conftest fixture
def test_flight_search_inputs(search_flight):
    print('\n\nPASS: All filter fields are filled with correct values')
    print('PASS: Flight has been searched successfully')
