from playwright.sync_api import expect

class NewBookingPage:
    def __init__(self, page):
        self.page = page

        self.search_flight_heading = page.locator(
            'h2.section-heading',
            has_text='Search Flights'
        )

    def verify_search_flight_heading(self):
        expect(self.search_flight_heading).to_be_visible()
        return self.search_flight_heading.inner_text().strip()