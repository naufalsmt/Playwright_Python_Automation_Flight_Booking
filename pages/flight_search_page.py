
class FlightSearchPage:
    def __init__(self, page):
        self.page = page

        self.flight_from = page.locator('#flight-from')
        self.flight_to = page.locator('#flight-to')
        self.departure_date = page.locator('#flight-departure-date')
        self.return_date = page.locator('#flight-return-date')
        self.passenger_count = page.locator('#flight-passengers')
        self.flight_class = page.locator('#flight-class')
        self.one_way = page.locator('#flight-one-way')
        self.search_flight = page.locator('#flight-search')


    def navigate(self):
        url = 'https://www.qapractice.com/flight-booking-scenarios'
        self.page.goto(url)


    def verify_page_heading(self):
        heading = self.page.locator(
            'h2.section-heading'
        ).first
        return heading


    def select_flight_from(self, dep_city):
        self.flight_from.select_option(dep_city)


    def select_flight_to(self, arr_city):
        self.flight_to.select_option(arr_city)


    def enter_departure_date(self, dep_date):
        self.departure_date.fill(dep_date)


    def enter_return_date(self, ret_date):
        self.return_date.fill(ret_date)


    def enter_passenger_count(self, psg_count):
        self.passenger_count.fill(str(psg_count))


    def select_flight_class(self, flight_class):
        self.flight_class.select_option(flight_class)


    def check_one_way(self):
        self.one_way.check()


    def uncheck_one_way(self):
        self.one_way.uncheck()


    def click_search_flight(self):
        self.search_flight.click()

