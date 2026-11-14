from playwright.sync_api import expect

class PassengerDetailsPage:
    def __init__(self, page):
        self.page = page

        self.passenger_heading = page.locator(
            'h2.section-heading',
            has_text='Passenger details'
        )
        self.passenger_name = page.locator('#flight-passenger-name')
        self.passenger_email = page.locator('#flight-passenger-email')
        self.passenger_phone = page.locator('#flight-passenger-phone')
        self.continue_payment_button = page.get_by_role(
            'button',
            name='Continue to payment →'
        )
        self.form = page.locator("form")


    def verify_passenger_details_page(self):
        expect(self.passenger_heading).to_be_visible()
        return self.passenger_heading.inner_text().strip()


    def enter_passenger_name(self, pass_name):
        self.passenger_name.fill(pass_name)


    def get_passenger_name(self):
        return self.passenger_name.input_value()


    def enter_passenger_email(self, pass_email):
        self.passenger_email.fill(pass_email)


    def get_passenger_email(self):
        return self.passenger_email.input_value()


    def enter_passenger_mobile(self, pass_mobile):
        self.passenger_phone.fill(str(pass_mobile))


    def get_passenger_mobile(self):
        return self.passenger_phone.input_value()


    def clear_passenger_form_field(self):
        self.passenger_name.clear()
        self.passenger_email.clear()
        self.passenger_phone.clear()


    def click_continue_to_payment(self):
        self.continue_payment_button.click()


    def form_validation(self):
        return self.form.inner_text()


    def verify_payment_button(self):
        expect(self.continue_payment_button).to_be_visible()