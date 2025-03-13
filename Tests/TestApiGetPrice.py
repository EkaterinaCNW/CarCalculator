import pytest

from ApiGetPrice import get_gas_price, get_power_price


class TestAPI:

    @pytest.mark.parametrize('function', [get_gas_price, get_power_price])
    def test_get_price(self, function):
        res = function()
        assert isinstance(res, int) or isinstance(res, float)