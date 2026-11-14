from playwright.sync_api import expect


class BookingConfirmationPage:
    def __init__(self, page):
        self.page = page

        self.success_heading = page.locator(
            "h2.text-success",
            has_text="Booking Confirmed!"
        )
        self.pnr_email = page.locator(".text-muted").nth(1)
        self.confirmation_details = page.locator("body")
        self.total_paid = page.get_by_text(
            "Total paid (Business)",
            exact=True
        )
        self.new_booking = page.get_by_role(
            'button',
            name='Book another flight'
        )


    def verify_success_booking_heading(self):
        expect(self.success_heading).to_be_visible()


    def get_confirmation_details(self):
        return self.confirmation_details.inner_text()


    def get_booking_ref(self):
        confirmation_txt = self.pnr_email.inner_text()
        return confirmation_txt.split("Booking reference ")[1].split(" ·")[0]


    def get_confirmation_email(self):
        confirmation_txt = self.pnr_email.inner_text()
        return confirmation_txt.split("sent to ")[1].strip().rstrip(".")


    def get_total_paid(self):
        amount = self.total_paid.locator("xpath=following-sibling::span")
        return amount.inner_text()


    def verify_new_booking_button(self):
        expect(self.new_booking).to_be_visible()


    def click_new_booking(self):
        self.new_booking.click()