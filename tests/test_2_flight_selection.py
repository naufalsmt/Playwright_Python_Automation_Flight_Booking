from pages.flight_results_page import FlightResultsPage
from utils.flight_details import FlightDetails

def test_flight_result(search_flight):
    print('\n\nPASS: Flight has been searched successfully')

    flight_results = FlightResultsPage(search_flight)
    section_count = flight_results.get_section_count()
    assert section_count == 2, f'expected 2 but got {section_count}'
    print('PASS: Departure & Return section displayed correctly')

    departure_heading = flight_results.get_section_title(0)
    return_heading = flight_results.get_section_title(1)
    assert 'Departure' in departure_heading
    assert 'Return' in return_heading
    print('PASS: Both Departure and Return title has beem verified')

    departure_flights = flight_results.get_flights_in_section(0)
    return_flights = flight_results.get_flights_in_section(1)
    assert departure_flights.count() > 0
    assert return_flights.count() > 0
    print('PASS: Departure and Return flights displayed and verified')

    departure_details = flight_results.select_cheapest_flight(0)
    # print("\nSelected departure:\n", departure_details)
    return_details = flight_results.select_cheapest_flight(1)
    # print("Selected return:\n", return_details)

    flight = FlightDetails()
    flight.save_departure(departure_details)
    flight.save_return(return_details)

    selected_flights = {
        "departure": departure_details,
        "return": return_details
    }

    print("\nSELECTED FLIGHT SUMMARY:")
    print('Departure:', flight.get_departure())
    print('Return:', flight.get_return())

    assert selected_flights["departure"]["section"].startswith("Departure")
    assert selected_flights["return"]["section"].startswith("Return")

    assert selected_flights["departure"]["flight_name"] != ""
    assert selected_flights["return"]["flight_name"] != ""

    assert selected_flights["departure"]["price"] > 0
    assert selected_flights["return"]["price"] > 0

    print("PASS: Selected departure and return flight details verified")

    departure_price = flight_results.select_cheapest_flight(0)
    print(f"PASS: Cheapest departure flight selected: ${departure_price}")

    return_price = flight_results.select_cheapest_flight(1)
    print(f"PASS: Cheapest return flight selected: ${return_price}")

    continue_button = search_flight.get_by_role(
        "button",
        name="Continue to passenger details →"
    )

    assert continue_button.is_visible()
    assert continue_button.is_enabled()
    print('PASS: Continue button is visible and clickable')

    continue_button.click()

    assert search_flight.get_by_role(
        "heading",
        name="Passenger Details"
    ).is_visible()
    print('PASS: Passenger page displayed and verified')

