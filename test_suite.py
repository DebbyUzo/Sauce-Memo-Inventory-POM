import pytest
from selenium import webdriver

from ActionPage.Action import Action_Page

@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = Action_Page(driver)
    login_page.login_url("https://www.saucedemo.com/")
    return login_page

def test_login_page_on_automation_customer_service_website(login):
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_submit_button()
    login.click_saucelabsbackpeak()
    login.click_saucelabsbikelight()
    login.click_saucelabsbolttshirt()
    login.click_saucelabsonesie()
    login.click_test_allthethingstshirt()
