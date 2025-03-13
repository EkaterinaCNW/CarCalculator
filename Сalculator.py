class Calculator:
    def __init__(self, mileage = 15000, years = 3, year_loss = 10):
        """
        Калькулятор расходов на автомобиль
        :param mileage: пробег
        :param years: количество лет
        :param year_loss:
        """
        self.mileage = mileage
        self.cars =  dict()# Car: Year Price
        self.years = years
        self.year_loss = year_loss / 100

    def add_car(self, car):
        """
        Добавляет автомобиль в список
        :param car: автомобиль
        """
        year_cost = car.year_cost(self.mileage)
        price_per_year = car.price / self.years
        left_price = self.get_left_price(car) / self.years
        self.cars[car] = year_cost + price_per_year - left_price

    def get_left_price(self, car):
        """
        Получает начальную цену на автомобиль
        :param car: Автомобиль
        :return: Начальная цена
        """
        initial_price = car.price
        for i in range(self.years):
            initial_price -=initial_price * self.year_loss
        return initial_price

    def print_cars(self):
        """
        Выводит в консоль информацию об автомобиле
        :return: Название автомобиля: годая цена
        """
        for car, year_price in self.cars.items():
            print(f"{car.name}:\t\t{year_price}")