from selenium.webdriver.common.by import By

class LoginLocator:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "login-button")

class AddToCartLocator:
    SAUCELABSBACKPEAK = (By.ID, "add-to-cart-sauce-labs-backpack")
    SAUCELABSBIKELIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    SAUCELABSBOLTTSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    SAUCELABSFLEECEJACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    SAUCELABSONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    TESTALLTHETHINGSTSHIRTRED = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
