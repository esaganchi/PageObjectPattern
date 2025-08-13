from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def go_to_cart(self):
        self.click(self.CART_LINK)
