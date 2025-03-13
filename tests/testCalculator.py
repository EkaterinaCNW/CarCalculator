from apis import get_gas_price, get_power_price
import pytest
import random

from calculator import add_two_numbers

mileage = [1000, 1000]

class TestCar:

    def test_static_years_cost(self, car):
        res = car.static_year_cost()
        assert res == 10000

    @pytest.mark.parametrize('mileage', mileage)
    def test_dynamic_year_cost(self, car, mileage):
        res = car.dynamic_year_cost(1000)
        expected = car.fuel_economy * mileage / 100 * get_gas_price()
        assert res == expected

    @pytest.mark.parametrize('mileage', mileage)
    def test_year_cost(self, car, mileage):
        res = car.year_cost(1000)
        expected = car.static_year_cost() + car.dynamic_year_cost(mileage)
        assert res == expected

class TestElectricCar():

    @pytest.mark.parametrize('mileage', mileage)
    def test_dynamic_year_cost(self, mileage, electricCar):
        assert electricCar.dynamic_year_cost(mileage) == electricCar.power_consumption * mileage / 1000 * get_power_price()

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

class TestAPI:

    @pytest.mark.parametrize('function', [get_gas_price, get_power_price])
    def test_get_price(self, function):
        res = function()
        assert isinstance(res, int) or isinstance(res, float)

    # for i in range(1000):
    #     a = random.randint(0, 1000)
    #     b = random.randint(1, 1000)
    #     result = a / b

    @pytest.mark.parametrize(
        'a, b, result',
        [
            (10, 15, 0.66),
            (4, 2, 2),
            (100, 50, 2),
            (0, 5, 0)
        ]
    )
    def test_sum(a, b, result):
        # является ли утверждение верным
        res = add_two_numbers(a, b)
        assert res == result