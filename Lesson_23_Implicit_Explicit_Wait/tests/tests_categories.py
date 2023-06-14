# Тут пишемо тести для виконання
import time


class TestSignIn:
    def test_click_on_signin_button(self, sign_in):
        sign_in.signin_button()

    def test_putting_credentials(self, sign_in):
        sign_in.signin_button()
        sign_in.enter_login()
        sign_in.enter_password()

    def test_full_sign_in(self, sign_in):
        sign_in.signin_button()
        sign_in.enter_login()
        sign_in.enter_password()
        sign_in.authorize_button()


class TestWebSettings:
    def test_change_to_light_theme(self, website_settings):
        website_settings.change_to_light_theme()

    def test_change_to_normal_theme(self, website_settings):
        website_settings.change_to_normal_theme()

    def test_change_to_dark_theme(self, website_settings):
        website_settings.change_to_dark_theme()

    def test_change_to_old_theme(self, website_settings):
        website_settings.change_to_old_theme()

    def test_open_subscriptions(self, website_settings):
        website_settings.open_subscriptions()


class TestEndToEnd:
    def test_end_to_end(self, end_to_end):
        end_to_end.signing_in()
        end_to_end.play_episode()
        end_to_end.logging_out()
        time.sleep(5)
