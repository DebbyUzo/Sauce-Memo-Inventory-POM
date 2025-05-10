import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.locators_page import LoginLocator, AddToCartLocator, CheckoutLocator


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

class addToCartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_saucelabsbackpeak(self):
        click_saucelabsbackpeak = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocator.SAUCELABSBACKPEAK))
        click_saucelabsbackpeak.click()
        time.sleep(5)

    def click_saucelabsbikelight(self):
        click_saucelabsbikelight = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocator.SAUCELABSBIKELIGHT))
        click_saucelabsbikelight.click()
        time.sleep(5)

    def click_saucelabsbolttshirt(self):
        click_saucelabsbolttshirt = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocator.SAUCELABSBOLTTSHIRT))
        click_saucelabsbolttshirt.click()
        time.sleep(5)

    def click_saucelabsfleecejacket(self):
        click_saucelabsfleecejacket = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocator.SAUCELABSFLEECEJACKET))
        click_saucelabsfleecejacket.click()
        time.sleep(5)

    def click_saucelabsonesie(self):
        click_saucelabsonesie = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocator.SAUCELABSONESIE))
        click_saucelabsonesie.click()
        time.sleep(5)

    def click_testallthethingstshirtred(self):
        click_testallthethingstshirtred = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddToCartLocator.TESTALLTHETHINGSTSHIRTRED))
        click_testallthethingstshirtred.click()
        time.sleep(5)

class checkout:
    def __init__(self, driver):
        self.driver = driver

    def click_shoppingCartBadge(self):
        click_shoppingCartBadge = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocator.SHOPPINGCARTBADGE))
        click_shoppingCartBadge.click()
        time.sleep(5)

    def click_checkout(self):
        click_checkout = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocator.CHECKOUT))
        click_checkout.click()
        time.sleep(5)

    def enter_firstname(self, Debbie):
        enter_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocator.FIRSTNAME))
        enter_firstname.send_keys(Debbie)
        time.sleep(5)

    def enter_lastname(self, Ego):
        enter_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocator.LASTNAME))
        enter_lastname.send_keys(Ego)
        time.sleep(5)

    def enter_postalcode(self, postal_code):
        enter_postalcode = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocator.POSTALCODE))
        enter_postalcode.send_keys(postal_code)
        time.sleep(5)

    def click_continue(self):
        click_continue = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocator.CONTINUE))
        click_continue.click()
        time.sleep(5)

    def click_finish(self):
        click_finish = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(CheckoutLocator.FINISH))
        click_finish.click()
        time.sleep(5)