from helpers import check_page_header
from page_objects.ContactUsPage import ContactUsPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_contact_us_page(browser, url):
    browser.get(url + "index.php?route=information/contact")
    check_page_header(browser)

    # check similar title, page_name, product_name
    page_name = browser.find_element(*ContactUsPage.PAGE_NAME).text
    header_name = browser.find_element(*ContactUsPage.HEADER_NAME).text
    assert page_name == header_name == browser.title

    # validate all errors on empty fields
    browser.find_element(*ContactUsPage.SUBMIT_BTN).click()
    browser.find_element(*ContactUsPage.ERROR_NAME_MSG)
    browser.find_element(*ContactUsPage.ERROR_EMAIL_MSG)
    browser.find_element(*ContactUsPage.ERROR_ENQUIRY_MSG)

    # type correct in all fields and submit
    browser.find_element(*ContactUsPage.INPUT_NAME).send_keys('Name')
    browser.find_element(*ContactUsPage.INPUT_EMAIL).send_keys("user@mail.to")
    browser.find_element(*ContactUsPage.INPUT_ENQUIRY).send_keys("blablablablablablabla")
    old_url = browser.current_url
    browser.find_element(*ContactUsPage.SUBMIT_BTN).click()
    WebDriverWait(browser, 5).until(EC.url_changes(old_url))
