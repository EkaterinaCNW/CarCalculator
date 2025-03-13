from ApiGetPrice import get_power_price
from Car import Car


class ElectricCar(Car):
    def __init__(self, name: str, price: int, insurance_cost: int,
                 power_consumption: int):
        """
        Электрический Автомобиль
        :param name: Название
        :param price: Стоимость
        :param power_consumption: Мощность
        :param insurance_cost: Страховая стоимость
        """
        super().__init__(name = name,
                         price = price,
                         service_cost = 0,
                         fuel_economy = 0,
                         insurance_cost = insurance_cost)
        self.power_consumption = power_consumption # Wt / 1

    def dynamic_year_cost(self, mileage: int):
        """
        Расчитывает ежегодные непостоянные затраты на автомобиль
        :param mileage: Пробег
        :return: Сумма затрат
        """
        return self.power_consumption * mileage / 1000 * get_power_price()