class FlightResultsPage:
    def __init__(self, page):
        self.page = page

        self.section_headings = page.locator("h5.fw-bold.mb-3")
        self.flight_cards = page.locator(".hover-lift")
        self.continue_button = page.get_by_role(
            "button",
            name="Continue to passenger details →"
        )


    def get_section_count(self):
        return self.section_headings.count()


    def get_section_title(self, index):
        heading = self.section_headings.nth(index)
        return " ".join(heading.inner_text().split())


    def get_flights_in_section(self, index):
        heading = self.section_headings.nth(index)
        section = heading.locator("xpath=following-sibling::*[1]")
        return section.locator(".hover-lift")


    def get_flight_price(self, flight):
        price = flight.locator('text=/\\$\\d+/').inner_text()
        return int(price.replace('$', ''))


    def get_cheapest_flight(self, section_index):
        flights = self.get_flights_in_section(section_index)

        flight_prices = []

        for i in range(flights.count()):
            flight = flights.nth(i)
            price = self.get_flight_price(flight)
            flight_prices.append(price)

        cheapest_price = min(flight_prices)
        cheapest_index = flight_prices.index(cheapest_price)
        cheapest_flight = flights.nth(cheapest_index)
        return cheapest_flight, cheapest_price


    def select_cheapest_flight(self, section_index):
        cheapest_flight, cheapest_price = self.get_cheapest_flight(section_index)
        selected_details = self.get_flight_details(cheapest_flight)
        selected_details["section"] = self.get_section_title(section_index)
        cheapest_flight.locator("button").click()
        return selected_details

    def click_continue_to_passenger(self):
        self.continue_button.click()


    def get_first_departure_route(self):
        departure_flight = self.get_flights_in_section(0)
        first_flight = departure_flight.nth(0)
        flight_details = first_flight.inner_text().splitlines()
        return flight_details[1].strip()


    def get_flight_details(self, flight):
        flight_details = flight.inner_text().splitlines()

        flight_name = flight_details[0].strip()
        route = flight_details[1].strip()
        price = self.get_flight_price(flight)

        return {
            "flight_name": flight_name,
            "route": route,
            "price": price
        }

