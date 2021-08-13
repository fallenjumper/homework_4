from selenium.webdriver.common.by import By


class HeaderElements:
    TOP_MENU_LIST = (By.CSS_SELECTOR, ".navbar-nav > li > a")
    SEARCH_TEXTBOX = (By.CSS_SELECTOR, "#search > input")
    TOP_MENU_DROPDOWN_LIST = (By.CSS_SELECTOR, ".dropdown-inner > ul > li > a")
    PAGE_NAME = (By.CSS_SELECTOR, ".breadcrumb > li > a[href*='product']")
