from Lesson_17_Cloaking_Incapsulation_Polymorphism.lesson_17_Istominov import VaticanMuseums, DuLouvre, Painting
import pytest


@pytest.mark.smoke
def test_check_add_visitors():
    exhibition_01 = VaticanMuseums()
    visitors_beginning = exhibition_01.visitors()
    visitors_end = exhibition_01.visitors()
    assert visitors_end - 10 == visitors_beginning


@pytest.mark.smoke
def test_author_name(painting_1):
    assert painting_1.painting_author == 'Van Gogh'


@pytest.mark.regression
def test_painting_name(painting_1):
    assert painting_1.painting_name == 'Korenveld met kraaien'


@pytest.mark.regression
def test_initial_price(painting_1):
    initial_price = painting_1.painting_price
    assert painting_1.painting_price == initial_price
    assert painting_1.painting_price == 10000


def test_price_change(painting_1, monkeypatch):
    monkeypatch.setattr(painting_1, 'painting_price', 50000)
    assert painting_1.painting_price == 50000
