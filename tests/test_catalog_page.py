import pytest
from helpers import check_page_header
from page_objects.HeaderElements import HeaderElements
from page_objects.CatalogPage import CatalogPage
from page_objects.MainPage import MainPage
from selenium.webdriver.support.select import Select


@pytest.mark.parametrize("catalog_id", [24, 18])
def test_catalog_page(browser, url, catalog_id):
    browser.get(url + f"index.php?route=product/category&path={catalog_id}")
    check_page_header(browser)

    # check similar title, page_name, product_name
    page_name = browser.find_element(*HeaderElements.PAGE_NAME).text
    catalog_name = browser.find_element(*CatalogPage.CATALOG_NAME).text
    assert page_name == catalog_name == browser.title

    # get all thumbs
    all_thumbs = browser.find_elements(*MainPage.PRODUCT_THUMB)

    # check correct count product thumbs and bottom counter
    count_thumbs = len(all_thumbs)
    text_bottom_counter = browser.find_element(*CatalogPage.BOTTOM_COUNTER).text
    assert f"Showing 1 to {count_thumbs} of {count_thumbs} (1 Pages)" == text_bottom_counter

    # check counter on left menu
    assert f"{browser.title} ({count_thumbs})" == browser.find_element(*CatalogPage.LEFT_MENU_ACTIVE_LINK).text

    # check sort function
    old_sort = all_thumbs
    sort_selector = Select(browser.find_element(*CatalogPage.SORT_SELECTOR))
    sort_selector.select_by_index(2)
    assert old_sort != browser.find_elements(*MainPage.PRODUCT_THUMB)

    # change layout
    old_layout = browser.find_element(*CatalogPage.LAYOUT_CLASS).get_attribute("class").split(" ")[1]
    browser.find_element(*CatalogPage.LIST_VIEW_BTN).click()
    new_layout = browser.find_element(*CatalogPage.LAYOUT_CLASS).get_attribute("class").split(" ")[1]
    assert old_layout == "product-grid"
    assert new_layout == "product-list"
