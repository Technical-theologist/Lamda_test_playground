from src.Base_page.login import Login
from src.Tests.BaseTest import BaseTest
class Test_Login(BaseTest):
    def test_login(self):
        login= Login (self.driver)
        login.login()
        