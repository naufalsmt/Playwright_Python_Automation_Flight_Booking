import time

from playwright.sync_api import sync_playwright

def test_login():
    start_time = time.time()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://practice.expandtesting.com/login")

        page.locator('#username').fill('practice')
        page.locator('#password').fill('SuperSecretPassword!')
        page.locator("button[type='submit']").click()

        assert "Secure Area" in page.locator("h1").inner_text()

        print('Loging Successfull')

        browser.close()
    end_time = time.time()
    print(f'Time taken: {end_time - start_time:2f} seconds')



