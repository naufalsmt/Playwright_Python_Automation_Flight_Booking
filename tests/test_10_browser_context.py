def test_multiple_page_context(page):
    context = page.context
    page2 = context.new_page()
    context.add_cookies([
        {
            "name": "qa_session",
            "value": "test123",
            "url": "https://example.com"
        }
    ])

    print("Page 1 cookies:", page.context.cookies())
    print("Page 2 cookies:", page2.context.cookies())
    assert page.context.cookies() == page2.context.cookies()