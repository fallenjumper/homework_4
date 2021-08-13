from page_objects.MainPage import MainPage
from helpers import attribute_of_element_changed, check_page_header
from selenium.webdriver.support.wait import WebDriverWait


def test_main_page(browser, url):
    browser.get(url)
    check_page_header(browser)

    # check exist elements
    browser.find_element(*MainPage.TOP_IMAGE_SLIDER)
    browser.find_element(*MainPage.BOTTOM_IMAGE_SLIDER)

    # check slider is not static (top/bottom)
    WebDriverWait(browser, 5).until(attribute_of_element_changed(MainPage.TOP_SLIDER_CONTENT, "style"))
    WebDriverWait(browser, 5).until(attribute_of_element_changed(MainPage.BOTTOM_SLIDER_CONTENT, "style"))

    # get all thumbs
    product_thumbs = browser.find_elements(*MainPage.PRODUCT_THUMB)

    # check count product thumbs
    assert len(product_thumbs) == 4

    for _ in product_thumbs:
        # check exist elements in product thumb
        elements_of_product_item = _.find_elements_by_css_selector("div")
        assert elements_of_product_item[0].get_attribute("class") == "image"
        assert elements_of_product_item[1].get_attribute("class") == "caption"
        assert elements_of_product_item[2].get_attribute("class") == "button-group"

        # check count of elements in product thumb
        assert len(elements_of_product_item) == 3

        # check non empty description of product thumb
        assert elements_of_product_item[1].find_element_by_css_selector("p").text != ""
