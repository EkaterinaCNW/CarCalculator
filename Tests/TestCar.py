import pytest
from ApiGetPrice import get_gas_price

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