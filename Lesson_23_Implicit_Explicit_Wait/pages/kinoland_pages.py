# Тут прописуємо основні класи які будуть використовуватись і код виконання
import time
from Lesson_23_Implicit_Explicit_Wait.pages.base_page import BasePage
from selenium.webdriver.support.select import By


class SignIn(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.sign_in_button = (By.XPATH, '//div[@class="wrapper"]//button[contains(text(), "Войти")]')
        self.login_input_field = (By.XPATH, '//*[@id="login_name"]')
        self.pass_input_field = (By.XPATH, '//*[@id="login_password"]')
        self.authorize_button = (By.XPATH, '//div[@class="login__row"]//button[@title="Вход"]')
        self.login = 'andrey_lk93'
        self.password = 'beast13'
        self.sign_out_button = (By.XPATH, '//*[@id="user-menu"]/ul/li[7]/a/span')

    def signin_button(self):
        self._wait_until_element_appears_and_click(self.sign_in_button)

    def sign_out_button(self):
        self._wait_until_element_appears_and_click(self.sign_out_button)

    def enter_login(self):
        self._wait_until_element_appears_for_input(self.login_input_field, self.login)

    def enter_password(self):
        self._wait_until_element_appears_for_input(self.pass_input_field, self.password)

    def authorization(self):
        self._wait_until_element_appears_and_click(self.authorize_button)


class WebsiteSettings(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.light_theme = (By.XPATH, '//li[@data-theme="light2"]')
        self.normal_theme = (By.XPATH, '//li[@data-theme="normal"]')
        self.dark_theme = (By.XPATH, '//li[@data-theme="dark"]')
        self.old_theme = (By.XPATH, '//li[@data-theme="old"]')
        self.search_input = (By.XPATH, '//div[@class="wrapper"]//form/input[@placeholder="Ищи и на английском"]')
        self.subscriptions = (By.XPATH, '//*[@id="user-menu"]/ul/li[2]/a')
        self.input_info = 'мандалорец'
        self.select_option_from_search = (By.XPATH, '//*[@id="film-47594"]/a/div[1]')
        self.play_button = (By.XPATH, '//*[@id="overroll"]/div/form/button')
        self.history = (By.XPATH, '//*[@id="user-menu"]/ul/li[5]/a/span')
        self.most_popular = (By.XPATH, '//div[@class="wrapper"]//a[@href="/popular/"]')

    def open_history(self):
        self._wait_until_element_appears_and_click(self.history)

    def open_most_popular(self):
        self._wait_until_element_appears_and_click(self.most_popular)

    def click_play_button(self):
        self._wait_until_element_appears_and_click(self.play_button)

    def change_to_light_theme(self):
        self._wait_until_element_appears_and_click(self.light_theme)

    def change_to_normal_theme(self):
        self._wait_until_element_appears_and_click(self.normal_theme)

    def change_to_dark_theme(self):
        self._wait_until_element_appears_and_click(self.dark_theme)

    def change_to_old_theme(self):
        self._wait_until_element_appears_and_click(self.old_theme)

    def search_for_show(self):
        self._wait_until_element_appears_for_input_and_enter(self.search_input, self.input_info)

    def open_subscriptions(self):
        self._wait_until_element_appears_and_click(self.subscriptions)

    def select_option_from_search(self):
        self._wait_until_element_appears_and_click(self.select_option_from_search)


class EndToEnd(SignIn, WebsiteSettings):
    def __init__(self, driver):
        super().__init__(driver)

    def signing_in(self):
        SignIn.signin_button(self)
        SignIn.enter_login(self)
        SignIn.enter_password(self)
        SignIn.authorization(self)

    def open_tv_show_main_page(self):
        WebsiteSettings.search_for_show(self)
        WebsiteSettings.select_option_from_search(self)
        WebsiteSettings.click_play_button(self)
        time.sleep(2)

    def widget_check(self):
        WebsiteSettings.change_to_normal_theme(self)
        time.sleep(2)
        WebsiteSettings.open_subscriptions(self)
        time.sleep(2)
        WebsiteSettings.change_to_light_theme(self)
        time.sleep(2)
        WebsiteSettings.open_history(self)
        time.sleep(2)
        WebsiteSettings.change_to_old_theme(self)
        WebsiteSettings.change_to_dark_theme(self)
        time.sleep(2)
        WebsiteSettings.open_most_popular(self)
        time.sleep(2)

    def logging_out(self):
        SignIn.sign_out_button(self)
        time.sleep(2)
