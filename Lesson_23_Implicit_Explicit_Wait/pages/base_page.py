# Тут пишемо функції expected conditions які стосуються дій які ми будемо використовувати
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self._web_driver_wait = WebDriverWait(self._driver, 5)

    def _wait_until_element_appears_and_click(self, locator):
        self._driver.implicitly_wait(2)
        self._web_driver_wait.until(EC.presence_of_element_located(locator)).click()


    def _wait_until_element_appears_for_input(self, locator, keys):
        data = self._web_driver_wait.until(EC.presence_of_element_located(locator))
        return data.send_keys(keys)

    def _wait_until_element_appears_for_input_and_enter(self, locator, keys):
        data = self._web_driver_wait.until(EC.presence_of_element_located(locator))
        return data.send_keys(keys, Keys.ENTER)

