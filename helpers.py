from page_objects.HeaderElements import HeaderElements


class attribute_of_element_changed:
    def __init__(self, locator, attr):
        self.locator = locator
        self.attr = attr
        self.old_attr = []

    def __call__(self, driver):
        # фиксируем текущее значение атрибута и начинаем сверять на следующем цикле
        if not self.old_attr:
            self.old_attr = driver.find_element(*self.locator).get_attribute(self.attr)
            return False

        # если текущее значение атрибута на экране не равно исходному -> True
        if self.old_attr != driver.find_element(*self.locator).get_attribute(self.attr):
            return True
        return False


def check_page_header(browser):
    # check placeholder on search box
    assert browser.find_element(*HeaderElements.SEARCH_TEXTBOX).get_attribute("placeholder") == "Search"

    # check list menu elements
    menu_elements = browser.find_elements(*HeaderElements.TOP_MENU_LIST)
    target_list_menu = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs",
                        "Cameras",
                        "MP3 Players"]
    current_list_menu = [i.text for i in menu_elements]
    assert target_list_menu == current_list_menu

    # check default not visibility items under menu
    dropdown_top_menu_lst = browser.find_elements(*HeaderElements.TOP_MENU_DROPDOWN_LIST)
    if not dropdown_top_menu_lst:
        raise ValueError("Не найден элемент")
    for element in dropdown_top_menu_lst:
        assert not element.is_displayed()
