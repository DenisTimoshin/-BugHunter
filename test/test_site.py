from pages.homepage import HomePage


def test(browser):
    home_page = HomePage(browser)
    home_page.open()
