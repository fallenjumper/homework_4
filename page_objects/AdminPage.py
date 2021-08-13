from selenium.webdriver.common.by import By


class AdminPage:
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    FORGOTTEN_PASS_LINK = (By.CSS_SELECTOR, ".help-block > a")
    HEADER_TITLE = (By.CSS_SELECTOR, ".panel-title")
    SUBMIT_BTN = (By.CSS_SELECTOR, ".btn.btn-primary")
