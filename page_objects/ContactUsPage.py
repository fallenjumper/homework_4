from selenium.webdriver.common.by import By


class ContactUsPage:
    PAGE_NAME = (By.CSS_SELECTOR, ".breadcrumb > li > a[href*='contact']")
    HEADER_NAME = (By.CSS_SELECTOR, ".row > div > h1")
    INPUT_NAME = (By.CSS_SELECTOR, "#input-name")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#input-email")
    INPUT_ENQUIRY = (By.CSS_SELECTOR, "#input-enquiry")
    ERROR_NAME_MSG = (By.XPATH, "//div[contains(text(), 'Name must be between 3 and 32 characters!')]")
    ERROR_EMAIL_MSG = (By.XPATH, "//div[contains(text(), 'E-Mail Address does not appear to be valid!')]")
    ERROR_ENQUIRY_MSG = (By.XPATH, "//div[contains(text(), 'Enquiry must be between 10 and 3000 characters!')]")
    SUBMIT_BTN = (By.CSS_SELECTOR, ".btn.btn-primary")
