from playwright.sync_api import expect

from pages.flight_results_page import FlightResultsPage
from pages.passenger_details_page import PassengerDetailsPage


def test_passenger_details(search_flight):
    print('\n\nPASS: Flight has been searched successfully')

    flight_results = FlightResultsPage(search_flight)
    flight_results.select_cheapest_flight(0)
    flight_results.select_cheapest_flight(1)
    flight_results.click_continue_to_passenger()

    passenger_details = PassengerDetailsPage(search_flight)
    passenger_details.verify_passenger_details_page()

    name = 'sachin'
    email = 'sachin@mail.com'
    invalid_email = 'sachin@mail'
    mobile = '+971525234667'

    passenger_details.enter_passenger_name(name)
    passenger_details.enter_passenger_email(email)
    passenger_details.enter_passenger_mobile(mobile)

    passenger_name = passenger_details.get_passenger_name()
    passenger_email = passenger_details.get_passenger_email()
    passenger_mobile = passenger_details.get_passenger_mobile()

    assert passenger_name == name
    assert passenger_email == email
    assert passenger_mobile == mobile

    print("PASS: Passenger details entered and verified successfully")

    passenger_details.clear_passenger_form_field()
    passenger_details.click_continue_to_payment()
    validation_txt = passenger_details.form_validation()

    assert 'Please enter the traveller name.' in validation_txt
    assert 'Please enter an email.' in validation_txt
    assert 'Please enter a phone number.' in validation_txt

    passenger_details.verify_passenger_details_page()
    print('PASS: Validation text displayed correctly for empty fields')

    passenger_details.enter_passenger_name(name)
    passenger_details.enter_passenger_email(invalid_email)
    passenger_details.enter_passenger_mobile(mobile)
    passenger_details.click_continue_to_payment()

    passenger_details.form_validation()
    validation_txt = passenger_details.form_validation()

    assert 'Please enter the traveller name.' not in validation_txt
    assert 'Enter a valid email address.' in validation_txt
    assert 'Please enter a phone number.' not in validation_txt

    print('PASS: Invalid email format validation text displayed correctly')

    passenger_details.enter_passenger_name(name)
    passenger_details.enter_passenger_email(email)
    passenger_details.enter_passenger_mobile(mobile)
    passenger_details.verify_payment_button()
    print('PASS: Payment button displayed correctly')

    passenger_details.click_continue_to_payment()
    payment_heading = search_flight.locator(
        "h2.section-heading",
        has_text="Payment"
    )

    expect(payment_heading).to_be_visible()
    actual_title = payment_heading.inner_text().strip()
    assert actual_title == "Payment"
    print("PASS: Payment page loaded successfully.")

    print('PASS: Passenger detail page successfully validated')
