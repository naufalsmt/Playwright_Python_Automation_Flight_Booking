from playwright.sync_api import expect

from pages.flight_results_page import FlightResultsPage
from pages.passenger_details_page import PassengerDetailsPage
from pages.payment_page import PaymentPage


def test_payment_page(search_flight):
    print('\n\nPASS: Flight has been searched successfully')

    flight_results = FlightResultsPage(search_flight)
    flight_results.select_cheapest_flight(0)
    flight_results.select_cheapest_flight(1)
    flight_results.click_continue_to_passenger()

    passenger_details = PassengerDetailsPage(search_flight)
    passenger_details.verify_passenger_details_page()

    name = 'sachin'
    email = 'sachin@mail.com'
    mobile = '+971525234667'

    passenger_details.enter_passenger_name(name)
    passenger_details.enter_passenger_email(email)
    passenger_details.enter_passenger_mobile(mobile)
    passenger_details.verify_payment_button()
    print('PASS: payment button displayed correctly')

    passenger_details.click_continue_to_payment()

    payment_page = PaymentPage(search_flight)
    payment_page.verify_payment_page_heading()
    print('PASS: Payment page displayed correctly')
    payment_page.verify_booking_summary()
    print('PASS: Booking summary displayed correctly')
    summary = payment_page.get_booking_summary_details()

    assert "AeroLink (AL248)" in summary, f'different departure flight displayed'
    assert "AeroLink (AL348)" in summary, f'different return flight displayed'
    assert "2 passengers" in summary, f'different number of passengers displayed'
    assert "Business" in summary, f'different flight class displayed'

    print("PASS: Booking summary details are verified correctly")

    card_number= '4000000000000001'
    exp_date= '10/30'
    cvv = '123'

    payment_page.click_pay_button()
    validation_txt = payment_page.verify_card_validation()

    assert 'Please enter the card number.' in validation_txt
    assert 'Please enter the expiry date.' in validation_txt
    assert 'Please enter the CVV.' in validation_txt

    print('PASS: Empty card payment - fields validation verified successfully')

    payment_page.enter_card_number(card_number)
    payment_page.enter_card_expiry(exp_date)
    payment_page.enter_card_cvv(cvv)
    payment_page.verify_pay_button()
    print('PASS: Payment button displayed correctly')

    payment_page.click_pay_button()
    success_heading = search_flight.locator(
        "h2.text-success",
        has_text="Booking Confirmed!"
    )
    expect(success_heading).to_be_visible()
    actual_success_title = success_heading.inner_text().strip()
    assert actual_success_title == "Booking Confirmed!"
    print("PASS: Booking confirmed page loaded successfully.")

    print('PASS: Payment page successfully validated')

