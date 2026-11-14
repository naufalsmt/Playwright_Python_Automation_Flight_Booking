from playwright.sync_api import expect


class PaymentPage:
    def __init__(self, page):
        self.page = page

        self.payment_heading = page.locator(
            "h2.section-heading",
            has_text="Payment"
        )
        self.card_number = page.locator('#flight-card-number')
        self.card_expiry = page.locator('#flight-expiry')
        self.card_cvv = page.locator('#flight-cvv')
        self.pay_button = page.locator('#flight-book')
        self.form = page.locator("form")
        self.booking_summary = page.locator(
            ".bg-light.border-0.mb-4.card"
        )
        self.total_amount = page.locator('[data-testid="flight-total"]')

    def verify_payment_page_heading(self):
        expect(self.payment_heading).to_be_visible()
        return self.payment_heading.inner_text().strip()


    def verify_booking_summary(self):
        expect(self.booking_summary).to_be_visible()


    def get_booking_summary_details(self):
        return self.booking_summary.inner_text()


    def enter_card_number(self, card_number):
        self.card_number.fill(str(card_number))


    def get_card_number(self):
        return self.card_number.input_value()


    def enter_card_expiry(self, card_expiry):
        self.card_expiry.fill(str(card_expiry))


    def get_card_expiry(self):
        return self.card_expiry.input_value()


    def enter_card_cvv(self, card_cvv):
        self.card_cvv.fill(str(card_cvv))


    def get_card_cvv(self):
        return self.card_cvv.input_value()


    def verify_pay_button(self):
        expect(self.pay_button).to_be_visible()
        expect(self.pay_button).to_be_enabled()


    def click_pay_button(self):
        self.pay_button.click()


    def verify_card_validation(self):
        return self.form.inner_text()


    def get_total_amount(self):
        amount_text = self.total_amount.inner_text()
        return int(amount_text.replace("$", ""))


