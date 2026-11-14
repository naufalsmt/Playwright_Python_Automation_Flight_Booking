class FlightDetails:

    def __init__(self):
        self.departure = {}
        self.return_flight = {}
        self.passenger_count = 0
        self.flight_class = ""

    def save_departure(self, details):
        self.departure = details

    def save_return(self, details):
        self.return_flight = details

    def save_booking_details(self, passenger_count, flight_class):
        self.passenger_count = passenger_count
        self.flight_class = flight_class

    def get_departure(self):
        return self.departure

    def get_return(self):
        return self.return_flight

    def get_passenger_count(self):
        return self.passenger_count

    def get_flight_class(self):
        return self.flight_class