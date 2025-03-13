import pytest

class TestCalculator():

    def test_add_car(self, calculator, car):
        calculator.add_car(car)
        assert calculator.cars
        assert car in calculator.cars
        assert calculator.cars[car] > 0

    def test_print_cars(self, calculator):
        calculator.print_cars()

    def test_get_left_price(self, calculator, car):
        res = calculator.get_left_price(car)
        assert res