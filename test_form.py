import time
import pytest
import settings
import locators
from base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By


def test_form(browser):
    """Проверяем что мы на странице заполнения формы"""
    only_page = BasePage(browser)
    check_page = only_page.go_to_site()

    assert 'Заполните анкету' in check_page


@pytest.mark.parametrize("name",
                         ['Иван', 'Ivan', 111, 'а', 255 * 'а'],
                         ids=["cyrillic", "latin", "numbers", "1 letters", "255 letters"])
def test_enter_name_valid(browser, name):
    """Проверяем ввод валидного значения имени"""
    name_field = BasePage(browser)
    name_field.go_to_site()
    result = name_field.enter_some(name, locator=locators.NAME_FIELD)
    time.sleep(1)

    assert type(result) == type('abc')


@pytest.mark.parametrize("name",
                         [' ', '', '@#$$%^', 256 * 'а'],
                         ids=["space", "empty", "special characters", "256 letters"])
def test_enter_invalid_name(browser, name):
    """Проверяем ввод невалидного значения имени"""
    name_field = BasePage(browser)
    check_name = BasePage(browser)
    name_field.go_to_site()
    name_field.enter_some(name, locator=locators.NAME_FIELD)
    time.sleep(1)
    result = check_name.check_name_field()

    assert result in ['Неверный формат', 'Обязательное поле', 'Превышено максимальное количество символов']


def test_all_field(browser):
    """Проверяем заполнение всех доступны полей формы"""
    only_page = BasePage(browser)
    only_page.go_to_site()
    only_page.enter_some(settings.valid_name_1, locators.NAME_FIELD)
    only_page.enter_some(settings.valid_email, locators.EMAIL_FIELD)
    only_page.enter_some(settings.valid_phone, locators.PHONE_FIELD)
    only_page.enter_some(settings.valid_company, locators.COMPANY_FIELD)
    only_page.find_element(locators.COMP_OF_WORKS).click()
    only_page.enter_some(settings.about_project, locators.ABOUT_PROJECT)
    only_page.find_element(locators.BUDGET).click()
    only_page.find_element(locators.SURVEY).click()
    iframe = browser.find_element(By.TAG_NAME, "iframe")
    scroll_origin = ScrollOrigin.from_element(iframe)
    ActionChains(browser).scroll_from_origin(scroll_origin, 0, 50).perform()

    time.sleep(3)
# К сожалению не могу преодолеть капчу, поэтому тест заканчивается таким образом.
# По уму надо поймать локатор со страницы отправленной формы и по нему судить о статусе теста.
# Усли кто-то это прочитает и будет готов подсказать как побороть капчу (лучше не словами и конкретным кодом),
# буду очень признателен. Я опробовал кучу способов, но пока увы.