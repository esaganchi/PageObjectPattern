from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    REMOVE_BTN = (By.ID, "remove-sauce-labs-backpack")

    def get_cart_items(self):
        return [el.text for el in self.driver.find_elements(*self.CART_ITEM)]

    def remove_backpack(self):
        self.click(self.REMOVE_BTN)
