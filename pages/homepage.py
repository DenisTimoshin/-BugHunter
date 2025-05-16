from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        """
        Открывает страницу каталога.
        """
        url = "https://denistimoshin.github.io/-BugHunter/"
        self.browser.get(url)
