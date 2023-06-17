# Тут пишемо тести для виконання
import time


class TestSignIn:  # Перевірки для авторизації запускати окремо одну від одної(не класом)
    def test_click_on_signin_button(self, sign_in):
        sign_in.signin_button()
        time.sleep(1)

    def test_putting_credentials(self, sign_in):
        sign_in.enter_login()
        sign_in.enter_password()
        time.sleep(1)

    def test_full_sign_in(self, sign_in):
        sign_in.signin_button()
        sign_in.enter_login()
        sign_in.enter_password()
        time.sleep(2)
        sign_in.authorization()
        time.sleep(2)


class TestWebSettings:
    def test_change_to_light_theme(self, website_settings):
        website_settings.change_to_light_theme()
        time.sleep(2)

    def test_change_to_normal_theme(self, website_settings):
        website_settings.change_to_normal_theme()
        time.sleep(2)

    def test_change_to_dark_theme(self, website_settings):
        website_settings.change_to_dark_theme()
        time.sleep(2)

    def test_change_to_old_theme(self, website_settings):
        website_settings.change_to_old_theme()
        time.sleep(2)

    def test_open_subscriptions(self, end_to_end, website_settings):
        end_to_end.signing_in()
        website_settings.open_subscriptions()
        time.sleep(5)

    def test_open_history(self, website_settings):
        website_settings.open_history()
        time.sleep(2)

    def test_open_most_popular(self, website_settings):
        website_settings.open_most_popular()
        time.sleep(2)


class TestEndToEnd:
    def test_end_to_end(self, end_to_end):
        end_to_end.signing_in()
        end_to_end.open_tv_show_main_page()
        end_to_end.widget_check()
        end_to_end.logging_out()
        time.sleep(2)
