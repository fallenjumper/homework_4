from selenium.webdriver.common.by import By


class CatalogPage:
    CATALOG_NAME = (By.CSS_SELECTOR, ".row > div > h2")
    BOTTOM_COUNTER = (By.CSS_SELECTOR, ".text-right")
    SORT_SELECTOR = (By.CSS_SELECTOR, "#input-sort")
    LEFT_MENU_ACTIVE_LINK = (By.CSS_SELECTOR, ".list-group-item.active")
    LAYOUT_CLASS = (By.CSS_SELECTOR, ".product-layout")
    LIST_VIEW_BTN = (By.CSS_SELECTOR, "#list-view")
