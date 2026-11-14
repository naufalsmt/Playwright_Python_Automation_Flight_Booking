import time
from playwright.sync_api import sync_playwright


def test_launch_browser():
    start_time = time.time()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto("https://www.example.com")

        assert page.title() == 'Example Domain'

        print('Browser launched successfully')
        print('Page title:', page.title())

        browser.close()

    end_time = time.time()
    print(f'time taken: {end_time - start_time:2f} seconds')

