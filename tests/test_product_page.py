import pytest
from helpers import check_page_header
from page_objects.ProductPage import ProductPage
from page_objects.HeaderElements import HeaderElements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("product_id,cart_total", [(43, "2 item(s) - $1,204.00"), (44, "2 item(s) - $2,404.00")])
def test_product_page(browser, url, product_id, cart_total):
    browser.get(url + f"index.php?route=product/product&product_id={product_id}")
    check_page_header(browser)

    # check similar title, page_name, product_name
    page_name = browser.find_element(*HeaderElements.PAGE_NAME).text
    product_name = browser.find_element(*ProductPage.PRODUCT_NAME).text
    assert page_name == product_name == browser.title

    # click add to cart and check reaction (set 2 items)
    qty_input = browser.find_element(*ProductPage.QUANTITY_ITEMS_INPUT)
    qty_input.clear()
    qty_input.send_keys(2)
    assert qty_input.get_attribute("value") == '2'
    browser.find_element(*ProductPage.SUBMIT_BUTTON).click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(ProductPage.ADD_TO_CART_ALERT))
    assert browser.find_element(*ProductPage.CART_TOTAL_ROW).text == cart_total

    # wait loading big picture by click on thumbnail
    browser.find_element(*ProductPage.THUMBNAIL_PIC).click()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located(ProductPage.BIG_PIC_THUMBNAIL))
    # close after loading
    browser.find_element(*ProductPage.BIG_PIC_CLOSE_BTN).click()
    WebDriverWait(browser, 5).until_not(EC.visibility_of_element_located(ProductPage.BIG_PIC_THUMBNAIL))
