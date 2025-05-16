from pages.homepage import HomePage #test


def test(browser):
    home_page = HomePage(browser)
    home_page.open()
