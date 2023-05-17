from .code_for_testing import Human

class TestHuman:
    def test_check_growth(self):
        human = Human('Joshua', 50, 'Pink')
        human.grow()

        assert human.age == 51

    def test_change_hair_color(self):
        human = Human('Joshua', 50, 'Pink')
        human.change_hair_color('Blonde')

        assert human.color == 'Blonde'
