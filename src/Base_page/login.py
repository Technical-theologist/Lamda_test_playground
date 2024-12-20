from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_argument("--incognito")
driver=webdriver.Chrome(options)
driver.get("https://ecommerce-playground.lambdatest.io/")
my_account=driver.find_element(By.XPATH,"(//div[@class='info']//span[contains(text(), 'My account')])[2]")
hover=ActionChains(driver).move_to_element(my_account)
hover.perform()
driver.implicitly_wait(10)
login=driver.find_element(By.XPATH,"//span[@class='title' and contains(text(), 'Login')]")
login.click()
expcted_url="https://ecommerce-playground.lambdatest.io/index.php?route=account/login"
current_url=driver.current_url
assert current_url==expcted_url
print("Login Sucessfully")