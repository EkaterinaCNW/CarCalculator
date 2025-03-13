from ApiGetPrice import get_gas_price


class Car:
    def __init__(self,
                 name: str,
                 price: int,
                 fuel_economy: float,
                 service_cost: int,
                 insurance_cost: int):
        """
        Автомобиль
        :param name: Название
        :param price: Стоимость
        :param service_cost: Мощность
        :param fuel_economy: Расход топлива l / 100 km
        :param insurance_cost: Страховая стоимость
        """
        self.name = name
        self.price = price
        self.service_cost = service_cost
        self.fuel_economy = fuel_economy
        self.insurance_cost = insurance_cost

    def static_year_cost(self):
        """
        Рассчитывает ежегодные постоянные затраты на автомобиль
        :return: Сумма постоянных затрат
        """
        return self.service_cost + self.insurance_cost

    def dynamic_year_cost(self, mileage: int):
        """
        Рассчитывает ежегодные непостоянные затраты на автомобиль
        :param mileage: Пробег
        :return: Сумма непостоянных затрат
        """
        return self.fuel_economy * mileage / 100 * get_gas_price()

    def year_cost(self, mileage: int):
        """
        Рассчитывает ежегодные затраты на автомобиль суммарно
        :param mileage: пробег
        :return: Сумма затрат на автомобиль
        """
        return self.static_year_cost() + self.dynamic_year_cost(mileage)