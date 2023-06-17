# Тут прописуємо основні класи які будуть використовуватись і код виконання
import time
from Lesson_23_Implicit_Explicit_Wait.pages.base_page import BasePage
from selenium.webdriver.support.select import By
from selenium.webdriver.common.keys import Keys


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
        self.choose_player = (By.XPATH, '//*[@class="player-select"]/div[@data-name="voidboost"]')
        self.season_button = (By.XPATH, '//*[@id="selectors"]/span[1]/div/span')
        self.choose_season_1 = (By.XPATH, '//*[@id="selectors"]/span[1]/div/ul/li[1]')
        self.episode_button = (By.XPATH, '//*[@id="selectors"]/span[2]/div')
        self.choose_episode_1 = (By.XPATH, '//*[@id="selectors"]/span[2]/div/ul/li[1]')
        self.run_player_button = (By.XPATH, '//*[@id="oframeplayer"]/pjsdiv[1]/video')

    def start_movie(self):
        self._wait_until_element_appears_and_click(self.run_player_button)

    def activate_season_button(self):
        self._wait_until_element_appears_and_click(self.season_button)

    def select_season(self):
        self._wait_until_element_appears_and_click(self.choose_season_1)

    def activate_episode_button(self):
        self._wait_until_element_appears_and_click(self.episode_button)

    def select_episode(self):
        self._wait_until_element_appears_and_click(self.choose_episode_1)

    def select_player(self):
        required_frame = self._driver.find_element_by_xpath('//*[@id="film"]')
        self._driver.switch_to.frame(required_frame)
        self._wait_until_element_appears_and_click(self.choose_player)

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

    def play_episode(self):
        WebsiteSettings.search_for_show(self)
        WebsiteSettings.select_option_from_search(self)
        WebsiteSettings.click_play_button(self)
        time.sleep(3)
        WebsiteSettings.select_player(self)
        time.sleep(3)
        WebsiteSettings.activate_season_button(self)
        time.sleep(3)
        WebsiteSettings.select_season(self)
        time.sleep(3)
        WebsiteSettings.activate_episode_button(self)
        time.sleep(3)
        WebsiteSettings.select_episode(self)
        time.sleep(3)
        WebsiteSettings.start_movie(self)
        time.sleep(60)

    def logging_out(self):
        SignIn.sign_out_button(self)
