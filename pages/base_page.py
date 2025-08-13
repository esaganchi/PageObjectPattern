from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=5):
        self.find(locator, timeout).click()

    def type(self, locator, text, timeout=5):
        self.find(locator, timeout).send_keys(text)

    def get_text(self, locator, timeout=5):
        return self.find(locator, timeout).text
