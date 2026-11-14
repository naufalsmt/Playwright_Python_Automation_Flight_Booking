from playwright.sync_api import expect

from pages.flight_results_page import FlightResultsPage
from pages.new_booking_page import NewBookingPage
from pages.passenger_details_page import PassengerDetailsPage
from pages.payment_page import PaymentPage
from pages.booking_confirmation_page import BookingConfirmationPage

def test_new_booking_navigation(search_flight):
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

    card_number = '4000000000000001'
    exp_date = '10/30'
    cvv = '123'

    payment_page.enter_card_number(card_number)
    payment_page.enter_card_expiry(exp_date)
    payment_page.enter_card_cvv(cvv)
    payment_page.click_pay_button()

    confirmation_page = BookingConfirmationPage(search_flight)
    confirmation_page.verify_success_booking_heading()
    print("PASS: Booking confirmed page loaded successfully.")

    confirmation_page.click_new_booking()
    expect(search_flight).to_have_url(
        "https://www.qapractice.com/flight-booking-scenarios"
    )
    print('PASS: New booking successfully navigate to search flight page')

    new_booking = NewBookingPage(search_flight)
    new_booking.verify_search_flight_heading()
    print('PASS: Search flight page loaded successfully.')
    print('PASS: New booking navigation successfully verified')


