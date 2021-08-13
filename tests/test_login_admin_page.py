from page_objects.AdminPage import AdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_catalog_page(browser, url):
    browser.get(url + "admin")

    # check correct placeholder
    assert browser.find_element(*AdminPage.USERNAME_INPUT).get_attribute("placeholder") == "Username"

    # check password input type is pass
    assert browser.find_element(*AdminPage.PASSWORD_INPUT).get_attribute("type") == "password"

    # check correct link to restore password
    assert browser.find_element(*AdminPage.FORGOTTEN_PASS_LINK).get_attribute(
        "href") == f"{url}admin/index.php?route=common/forgotten"

    # check correct title header
    assert browser.find_element(*AdminPage.HEADER_TITLE).text == "Please enter your login details."

    # check submit button
    old_url = browser.current_url
    browser.find_element(*AdminPage.SUBMIT_BTN).click()
    WebDriverWait(browser, 5).until(EC.url_changes(old_url))
