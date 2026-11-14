from playwright.sync_api import sync_playwright, expect
import time

def test_flight_booking_form():
    start_time = time.time()

    # start the browser engine ans pass url in that browser
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless=True,
            args=['--start-maximized']
        )
        page = browser.new_page(no_viewport=True)
        page.goto("https://www.qapractice.com/flight-booking-scenarios")

        h1_title = 'Flight Booking Automation Practice'
        assert h1_title in page.locator('h1').inner_text()
        print('\nPASS: browser launched')

        # Validate search flight page title
        search_flight_title = page.locator(
            "h2.section-heading",
            has_text="Search Flights"
        )
        expect(search_flight_title).to_be_visible()
        actual_search_flight_title = search_flight_title.inner_text().strip()
        # print('actual title:', actual_search_flight_title)
        assert actual_search_flight_title == "Search Flights"
        print("PASS: Search Flight page loaded successfully.")

        """Validate each element 'route from and to, select date, passenger, class, one way, search button' 
        in search flight page"""
        flight_from = page.locator('#flight-from')
        flight_from.select_option('Dubai')
        assert flight_from.input_value() == 'Dubai'
        flight_to = page.locator('#flight-to')
        flight_to.select_option('London')
        assert flight_to.input_value() == 'London'
        departure_date = page.locator('#flight-departure-date')
        departure_date.fill('2026-11-10')
        assert departure_date.input_value() == '2026-11-10'
        return_date = page.locator('#flight-return-date')
        return_date.fill('2026-12-10')
        assert return_date.input_value() == '2026-12-10'
        passenger_count = page.locator('#flight-passengers')
        passenger_count.fill('2')
        assert passenger_count.input_value() == '2'
        flight_class = page.locator('#flight-class')
        flight_class.select_option('Business')
        assert flight_class.input_value() == 'Business'
        one_way = page.locator('#flight-one-way')
        one_way.check()
        assert one_way.is_checked()
        time.sleep(3)
        one_way.uncheck()
        assert not one_way.is_checked()
        search_flight = page.locator('#flight-search')
        search_flight.click()
        print('PASS: Search Flight button clicked successfully')

        # Validated the search flight section title
        search_page_title = "Departure · Dubai → London"
        heading = page.locator("h5.fw-bold.mb-3").first
        actual_title = " ".join(heading.inner_text().split())
        # print("Actual title:", actual_title)
        assert search_page_title == actual_title
        print('PASS: departure flight list title verified')

        # extract the flight list after search
        flights = page.locator('.hover-lift')
        total_flights = flights.count()
        # print("Total flights:", total_flights)
        flight_price = []
        for i in range(total_flights):
            flight = flights.nth(i)
            flight_details = flight.inner_text()
            # print(f"\nFlight {i + 1}:")
            # print(flight_details)
            assert total_flights > 0, f'No flight displays'

        # extract the flight price list from each list of flights
            price = flight.locator('text=/\\$\\d+/').inner_text()
            price_value = int(price.replace('$', ''))
            flight_price.append(price_value)
            # print(f'\nFlight {i + 1}, price: {price_value}')
            assert price_value > 100, f'less price found in flight {i + 1}: price: {price_value}'

        print('PASS: List of flight displayed')
        print('PASS: Flight price should not be less than $100')

        # extract cheapest price details
        lowest_price = min(flight_price)
        print(f'\nlowest price: {lowest_price}')
        lowest_price_index = flight_price.index(lowest_price)
        lowest_price_flight = flights.nth(lowest_price_index)
        print(f'\nlowest price flight details:')
        print(lowest_price_flight.inner_text())
        lowest_price_flight.locator('button').click()

        """
        # extract highest price detail
        highest_price = max(flight_price)
        print(f'\nhighest price: {highest_price}')
        highest_price_index = flight_price.index(highest_price)
        highest_price_flight = flights.nth(highest_price_index)
        print(f'\nhighest price flight details:')
        print(highest_price_flight.inner_text())
        """

        # extract the lowest flight detail from both departure and return section
        headings = page.locator("h5.fw-bold.mb-3")
        print("Total headings:", headings.count())
        for i in range(headings.count()):
            heading = headings.nth(i)

            section = heading.locator("xpath=following-sibling::*[1]")
            section_flights = section.locator(".hover-lift")

            section_prices = []
            for j in range(section_flights.count()):
                flight = section_flights.nth(j)

                price = flight.locator('text=/\\$\\d+/').inner_text()
                price_value = int(price.replace('$', ''))

                section_prices.append(price_value)

            cheapest_price = min(section_prices)
            cheapest_index = section_prices.index(cheapest_price)

            cheapest_flight = section_flights.nth(cheapest_index)

            print(f"\n{heading.inner_text()}")
            print("Cheapest price:", cheapest_price)
            print("Cheapest flight details:")
            print(cheapest_flight.inner_text())
            cheapest_flight.locator('button').click()

            # click on continue button were navigate to passenger detail page
            continue_button = page.get_by_role('button', name='Continue to passenger details →')
            # print('continue button enable:', continue_button.is_enabled())
            if continue_button.is_enabled():
                continue_button.click()

                # verify the title for passenger detail page
                passenger_heading = page.locator(
                    'h2.section-heading',
                    has_text='Passenger details'
                )
                expect(passenger_heading).to_be_visible()
                actual_title = passenger_heading.inner_text().strip()
                # print('actual title:', actual_title)
                assert actual_title == 'Passenger details'

                # fill the form and verify the input value
                passenger_name= page.locator('#flight-passenger-name')
                passenger_name.fill('Sachin')
                passenger_email = page.locator('#flight-passenger-email')
                passenger_email.fill('sachin@mail.com')
                passenger_phone = page.locator('#flight-passenger-phone')
                passenger_phone.fill('+971512345678')

                assert passenger_name.input_value() == 'Sachin'
                assert passenger_email.input_value() == 'sachin@mail.com'
                assert passenger_phone.input_value() == '+971512345678'

                print("\nPASS: Passenger details entered and verified successfully")

                # clear the input form fields
                passenger_name.clear()
                passenger_email.clear()
                passenger_phone.clear()

                # click on the continue to payment button
                continue_payment = page.get_by_role(
                    'button',
                    name='Continue to payment →'
                )
                continue_payment.click()

                # validate the error validation message
                form = page.locator("form")
                validation_txt = form.inner_text()

                assert 'Please enter the traveller name.' in validation_txt
                assert 'Please enter an email.' in validation_txt
                assert 'Please enter a phone number.' in validation_txt

                passenger_heading = page.locator(
                    "h2.section-heading",
                    has_text="Passenger details"
                )

                expect(passenger_heading).to_be_visible()

                print('PASS: validation text displayed correctly')

                # wrong email input and submit: verify the validation error message
                passenger_name.fill('Sachin')
                passenger_email.fill('sachin.com')
                passenger_phone.fill('+971512345678')
                continue_payment.click()
                time.sleep(5)

                form = page.locator("form")
                validation_txt = form.inner_text()

                assert 'Please enter the traveller name.' not in validation_txt
                assert 'Enter a valid email address.' in validation_txt
                assert 'Please enter a phone number.' not in validation_txt

                print('PASS: invalid email format validation text displayed correctly')

                # enter valid passenger details and navigate to payment page
                passenger_name.fill('Sachin')
                passenger_email.fill('sachin@mail.com')
                passenger_phone.fill('+971512345678')
                continue_payment.click()
                time.sleep(5)
                payment_heading = page.locator(
                    "h2.section-heading",
                    has_text="Payment"
                )

                expect(payment_heading).to_be_visible()
                actual_title = payment_heading.inner_text().strip()
                assert actual_title == "Payment"
                print("PASS: Payment page loaded successfully.")

                # Enter card details
                card_number = page.locator('#flight-card-number')
                card_expiry = page.locator('#flight-expiry')
                card_cvv = page.locator('#flight-cvv')
                submit_button = page.locator('#flight-book')
                submit_button.click()

                form = page.locator("form")
                validation_txt = form.inner_text()

                assert 'Please enter the card number.' in validation_txt
                assert 'Please enter the expiry date.' in validation_txt
                assert 'Please enter the CVV.' in validation_txt

                print('PASS: missing card details validation text displayed correctly')

                # Enter valid card detail and submit payment and navigate to confirmation page
                card_number.fill('4000000000000002')
                card_expiry.fill('10/20')
                card_cvv.fill('123')
                submit_button.click()

                # verify the title of confirmation page
                success_heading = page.locator(
                    "h2.text-success",
                    has_text="Booking Confirmed!"
                )
                expect(success_heading).to_be_visible()
                actual_success_title = success_heading.inner_text().strip()
                assert actual_success_title == "Booking Confirmed!"
                print("PASS: Booking confirmed page loaded successfully.")

                # extract booking reference and booking email from confirmation text
                pnr_email = page.locator(".text-muted").nth(1)
                confirmation_text = pnr_email.inner_text()

                # print("Confirmation details:", confirmation_text)

                booking_reference = confirmation_text.split("Booking reference ")[1].split(" ·")[0]
                confirmed_email = confirmation_text.split("sent to ")[1].strip().rstrip(".")

                assert booking_reference != ""
                assert confirmed_email == "sachin@mail.com"

                # print("Booking reference:", booking_reference)
                # print("Confirmed email:", confirmed_email)
                print("PASS: Booking reference and email verified.")

                # verify the booking flight details
                confirmation_text = page.locator("body").inner_text()

                assert "AeroLink (AL248)" in confirmation_text
                assert "Dubai → London" in confirmation_text

                assert "AeroLink (AL348)" in confirmation_text
                assert "London → Dubai" in confirmation_text

                print("PASS: Departure and return flights verified.")

                # verify total amount has been paid
                total_paid = page.get_by_text(
                    "Total paid (Business)",
                    exact=True
                )

                amount = total_paid.locator("xpath=following-sibling::span")
                amount_text = amount.inner_text()
                # print("Total paid:", amount_text)

                assert amount_text.startswith("$")
                assert int(amount_text.replace("$", "")) > 0

                print("PASS: Total payment verified.")

                # navigate to new booking flight page
                new_booking = page.get_by_role(
                    'button',
                    name='Book another flight'
                )
                new_booking.click()
                assert actual_search_flight_title == "Search Flights"
                print("PASS: Search Flight page loaded successfully.")

        time.sleep(4)
        browser.close()

    end_time = time.time()
    print(f'\ntime taken: {end_time - start_time:2f} seconds')
