from src import Utils
# from src.Base_page import Base_page


class Login():
    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver

    def login(self):
        self.hover(Utils.web_helpers.locators.Locators.my_account)
        self.click_via_text("Login")
