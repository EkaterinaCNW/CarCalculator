from ApiGetPrice import get_power_price
import pytest

mileage = [1000, 1000]

class TestElectricCar():

    @pytest.mark.parametrize('mileage', mileage)
    def test_dynamic_year_cost(self, mileage, electricCar):
        assert electricCar.dynamic_year_cost(mileage) == electricCar.power_consumption * mileage / 1000 * get_power_price()