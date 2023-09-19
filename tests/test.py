import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division_succcess(self):
        assert self.calc.division(self, 15, 3) == 5

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 10, 1) == 9

    def test_adding_success(self):
        assert self.calc.adding(self, 4, 8) == 12

    def teardown(self):
        print('Выполнение метода Teardown.')
