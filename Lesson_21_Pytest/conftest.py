from Lesson_17_Cloaking_Incapsulation_Polymorphism.lesson_17_Istominov import Painting
import pytest


@pytest.fixture()
def painting_1():
    painting_01 = Painting('Van Gogh', 'Korenveld met kraaien', 10000)
    yield painting_01
