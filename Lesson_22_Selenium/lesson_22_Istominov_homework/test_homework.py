from selenium import webdriver
from selenium.webdriver import Chrome, Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_complex_actions_on_iherb():
# Тест 1 - Відкрити сайт iherb у пошуку в гугл (open_aromat_with_google_search)
    driver = Chrome('Lesson_22_Selenium/drivers/chromedriver.exe')
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get('https://google.com')
    time.sleep(5)
    search_input_field_locator = "//textarea[@title='Пошук']"
    search_input_field = driver.find_element(by='xpath', value=search_input_field_locator)
    search_input_field.send_keys('aromat')
    search_input_field.send_keys(Keys.ENTER)
    time.sleep(2)
    aromat_locator = '//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3'
    first_non_ad_link = driver.find_element(by='xpath', value=aromat_locator)
    first_non_ad_link.click()
    time.sleep(2)

# Тест 2 - Знайти парфуми у пошуку (test_search_for_Armani)
    search_input_field_aromat_locator = '//*[@id="header-search"]/form/div[1]/div[2]/input'
    search_input_field_aromat = driver.find_element(by='xpath', value=search_input_field_aromat_locator)
    search_input_field_aromat.send_keys('Armani')
    search_input_field_aromat.send_keys(Keys.ENTER)
    time.sleep(5)

# Тест 3 - Обрати таблетовану форму випуску (choose_tablets_in_sidebar)
    expand_button_locator = driver.find_element(By.XPATH, '//*[@id="m-more-less-left_semeystvo_aromatov"]/a[2]')
    driver.execute_script('arguments[0].scrollIntoView(true)', expand_button_locator)
    expand_button_locator.click()
    time.sleep(3)
    scent_button_locator = driver.find_element(By.XPATH, '//*[@id="narrow-by-list-0"]/dd[3]/ol/li[12]/a')
    scent_button_locator.click()
    time.sleep(3)

# Тест 4 - Відкрити деталі продукту (test_open_product_details)
    product_locator = driver.find_element(By.XPATH, '//*[@title="Armani Eau Pour Homme"]').click()
    time.sleep(3)

# Тест 6 - Додати товар до кошика (test_add_product_to_cart)
    add_to_cart_locator = driver.find_element(by='xpath', value='//*[@id="block-related"]/li/div/div/a').click()
    time.sleep(3)
    add_to_cart_locator_01 = driver.find_element(By.XPATH, '//*[@id="product_addtocart_form"]/div[3]/div[2]/div/div/\n'
                                                           'div[2]/button/span/span').click()
    time.sleep(2)
    confirm_button_locator = driver.find_element(By.XPATH, '//*[@id="success-checkout-button"]/span/span').click()
    time.sleep(5)
    driver.quit()


# driver.find_element(by=By.TAG_NAME, value='body').send_keys(Keys.PAGE_DOWN)
# time.sleep(1)
