from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class Base_page():
    def __init__(self,driver):
        self.driver=driver
    def find_element_by_text(self,text):
        try:
            print(f"//*[contains(text(), '{text}')]")
            element=self.driver.find_element(By.XPATH,f"//*[contains(text(),'{text}')]")
        except NoSuchElementException:
            print(f"'{text}'not found")
    def send_keys_via_place_holder(self,text):
        try:
            element=self.driver.find_element(By.XPATH, f"//input[@placeholder='{text}']")
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.DELETE)
            element.send_keys(text)
        except NoSuchElementException:
            print(f"'{text}'not found")
    def send_keys_via_xpath(self, xpath, text):
        try:
            element=self.driver.find_element(By.XPATH, xpath)
            element.send_keys(Keys.CONTROL + "a")
            element.send_keys(Keys.DELETE)
            element.send_keys(text)
        except NoSuchElementException:
            print(f"'{text}'not found")

    def hover(self,xpath=None,text=None):
        try:
            # If xpath is provided, use it to find the element
            if xpath:
                element = self.driver.find_element(By.XPATH, xpath)
            elif text:
                # If text is provided, find the element by text
                element = self.driver.find_element(By.XPATH, f"//*[text()='{text}']")
            else:
                print("Neither XPath nor text provided.")
                return
        except NoSuchElementException:
            print(f"Element with XPath '{xpath}' or text '{text}' not found.")
            return

            # Perform the hover action
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
    
    def click_via_text(self, text):
        try:
            element = self.driver.find_element(By.XPATH, f"//*[text()='{text}']")
            element.click()
        except NoSuchElementException:
            print(f"Element with text '{text}' not found.")
    
    def fluent_wait(driver,by_locator,time_out=10,poll_interval=1):
        try:
        
            wait = WebDriverWait(driver, timeout=10, polling_interval=1, ignored_exceptions=[Exception])
            element = wait.until(EC.presence_of_element_located(by_locator))
        except TimeoutException:
            print(f"Element with locator '{by_locator}' not found within {timeout} seconds.")
        
        except NoSuchElementException:
            print(f"Element with text '{text}' or XPath '{xpath}' not found.")
    def quit(self):
        self.driver.quit()



