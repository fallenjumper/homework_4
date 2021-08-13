from selenium.webdriver.common.by import By


class MainPage:
    TOP_IMAGE_SLIDER = (By.CSS_SELECTOR, "#slideshow0")
    TOP_SLIDER_CONTENT = (By.CSS_SELECTOR, "#slideshow0 > .swiper-wrapper")
    BOTTOM_IMAGE_SLIDER = (By.CSS_SELECTOR, "#carousel0")
    BOTTOM_SLIDER_CONTENT = (By.CSS_SELECTOR, "#carousel0 > .swiper-wrapper")
    PRODUCT_THUMB = (By.CSS_SELECTOR, ".product-thumb")
