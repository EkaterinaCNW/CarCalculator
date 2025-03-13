# fixture используют для чтение данных из файла
from calculator import Car, ElectricCar, Calculator
import pytest

@pytest.fixture()
def car():
    print("\nCreating a new car\n")
    return Car("Range Rover", 650000, 3, 3000, 7000)

@pytest.fixture
def electricCar():
    return ElectricCar("Tesla Model 3",  200000, 5500, 150)

@pytest.fixture(scope="session")
def calculator(car):
    res = Calculator()
    res.add_car(car)
    return res