# Тут прописуємо наші фікстури
from selenium.webdriver import Chrome
from Lesson_23_Implicit_Explicit_Wait.pages.kinoland_pages import SignIn, WebsiteSettings, EndToEnd
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome('Lesson_23_Implicit_Explicit_Wait/drivers/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://kinoland.biz')
    yield driver
    driver.quit()


@pytest.fixture
def sign_in(driver):
    yield SignIn(driver)


@pytest.fixture
def website_settings(driver):
    yield WebsiteSettings(driver)


@pytest.fixture
def end_to_end(driver):
    yield EndToEnd(driver)
