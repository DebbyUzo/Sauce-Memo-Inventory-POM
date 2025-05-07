import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.locators_page import LoginLocator

class Action_Page:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.USERNAME))
        enter_username.send_keys(username)
        time.sleep(5)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(5)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(5)

    def click_saucelabsbackpeak(self):
        click_saucelabsbackpeak = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.SAUCELABSBACKPEAK))
        click_saucelabsbackpeak.click()
        time.sleep(5)

    def click_saucelabsbikelight(self):
        click_saucelabsbikelight = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.SAUCELABSBIKELIGHT))
        click_saucelabsbikelight.click()
        time.sleep(5)

    def click_saucelabsbolttshirt(self):
        click_saucelabsbolttshirt = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.SAUCELABSBOLTTSHIRT))
        click_saucelabsbolttshirt.click()
        time.sleep(5)

    def click_saucelabsonesie(self):
        click_saucelabsonesie = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.SAUCELABSONESIE))
        click_saucelabsonesie.click()
        time.sleep(5)

    def click_test_allthethingstshirt(self):
        click_test_allthingstshirt = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.SAUCELABSBOLTTSHIRT))
        click_test_allthingstshirt.click()
        time.sleep(5)

    def click_shoppingcartbadge(self):
        click_shoppingcartbadge = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.SHOPPINGCARTBADGE))
        click_shoppingcartbadge.click()
        time.sleep(5)

    def click_checkout(self):
        click_checkout = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.CHECKOUT))
        click_checkout.click()
        time.sleep(5)

    def enter_firstname(self, Debbie):
        enter_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.FIRSTNAME))
        enter_firstname.send_keys(Debbie)
        time.sleep(5)

    def enter_lastname(self, Ego):
        enter_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.LASTNAME))
        enter_lastname.send_keys(Ego)
        time.sleep(5)

    def enter_postalcode(self,):
        enter_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.POSTALCODE))
        enter_postalcode.send_keys()
        time.sleep(5)

    def click_continue(self):
        click_continue = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.CONTINUE))
        click_continue.click()
        time.sleep(5)

    def click_finish(self):
        click_finish = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocator.FINISH))
        click_finish.click()
        time.sleep(5)