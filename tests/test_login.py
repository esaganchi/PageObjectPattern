from pages.login_page import LoginPage

def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")
    login_page.login("standard_user", "wrong_password")
    error = login_page.get_error_message()
    assert "Username and password do not match" in error
