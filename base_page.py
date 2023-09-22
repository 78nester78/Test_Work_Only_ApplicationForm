import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://only.digital/projects#brief'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'не найден {locator}')

    def go_to_site(self):
        self.driver.get(self.base_url)
        form = self.find_element(locators.START_PAGE)
        return form.text

    def enter_some(self, some, locator):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(some)
        return search_field.text

    def check_name_field(self):
        mail_field = self.find_element(locators.EMAIL_FIELD)
        mail_field.click()
        check_name = self.find_element(locators.WRONG_NAME)
        return check_name.text
