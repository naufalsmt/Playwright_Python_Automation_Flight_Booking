from utils.flight_details import FlightDetails


def test_flight_details():
    flights = FlightDetails()

    departure = {
        "flight_name": "AeroLink (AL248)",
        "route": "Dubai → London",
        "price": 304
    }

    return_flight = {
        "flight_name": "AeroLink (AL348)",
        "route": "London → Dubai",
        "price": 304
    }

    flights.save_departure(departure)
    flights.save_return(return_flight)

    print(flights.get_departure())
    print(flights.get_return())

    flights.save_booking_details(2, "Business")

    print("Passengers:", flights.get_passenger_count())
    print("Flight class:", flights.get_flight_class())