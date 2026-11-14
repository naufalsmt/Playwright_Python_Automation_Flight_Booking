from playwright.sync_api import expect

from pages.flight_results_page import FlightResultsPage
from pages.passenger_details_page import PassengerDetailsPage
from pages.payment_page import PaymentPage
from pages.booking_confirmation_page import BookingConfirmationPage

def test_booking_confirmation(search_flight):
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

    booking_ref = confirmation_page.get_booking_ref()
    # print('booking reference:', booking_ref)
    assert booking_ref.strip()
    print("PASS: Booking reference number loaded successfully.")

    booking_email = confirmation_page.get_confirmation_email()
    # print('booking email:', booking_email)
    assert booking_email == email
    print("PASS: Booking reference email loaded successfully.")

    booking_amount = confirmation_page.get_total_paid()
    # print('booking amount:', booking_amount)
    assert booking_amount.startswith("$")
    assert int(booking_amount.replace("$", "")) > 0
    print("PASS: Booking amount loaded successfully.")

    confirmation_detail = confirmation_page.get_confirmation_details()
    # print('confirmation detail:', confirmation_detail)
    assert "AeroLink (AL248)" in confirmation_detail
    assert "Dubai → London" in confirmation_detail

    assert "AeroLink (AL348)" in confirmation_detail
    assert "London → Dubai" in confirmation_detail
    print("PASS: Departure and return flights verified in the confirmation details.")

    assert "Total paid (Business)" in confirmation_detail
    assert "$1216" in confirmation_detail, f'Wrong amount displayed'
    print('PASS: Booking amount and flight type are correctly displayed in the confirmation details.')

    confirmation_page.verify_new_booking_button()
    print('PASS: New booking button displayed correctly')

    confirmation_page.click_new_booking()
    expect(search_flight).to_have_url(
        "https://www.qapractice.com/flight-booking-scenarios"
    )
    print('PASS: New booking successfully navigate to search flight page')

    print('PASS: Booking confirmation page verified successfully.')


