from selenium.webdriver.common.by import By


class ProductPage:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".row > div > h1")
    THUMBNAIL_PIC = (By.CSS_SELECTOR, ".thumbnail")
    BIG_PIC_THUMBNAIL = (By.CSS_SELECTOR, ".mfp-img")
    BIG_PIC_CLOSE_BTN = (By.CSS_SELECTOR, ".mfp-close")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    ADD_TO_CART_ALERT = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    CART_TOTAL_ROW = (By.CSS_SELECTOR, "#cart-total")
    QUANTITY_ITEMS_INPUT = (By.CSS_SELECTOR, "#input-quantity")
