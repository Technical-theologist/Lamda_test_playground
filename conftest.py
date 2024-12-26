import pytest
from selenium import webdriver
from src.Utils.api_helpers import urls

@pytest.fixture(params=["chrome"],scope="class")
def initialise_driver(request):
    driver=None
    if request.param=="chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        driver=webdriver.Chrome()
        # driver.maximize_window()
    # elif request.param=="firefox":
    #     options = webdriver.FirefoxOptions()
    #     options.add_argument("--incognito")
    #     driver=webdriver.Firefox(options)
    #     driver.maximize_window()
    # elif request.param=="edge":
    #     options = webdriver.EdgeOptions()
    #     options.add_argument("--incognito")
    #     driver=webdriver.Edge(options)
    #     driver.maximize_window()
    # else:
    #     print("Please select the browser")
    #     print(request.param)
    print("Browser",request.param)
    driver.get(urls.base_url)
    driver.maximize_window()
    request.cls.driver=driver
    yield driver
    driver.quit()
