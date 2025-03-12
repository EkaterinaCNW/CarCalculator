import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()

    calc.add_car(
        calculator.ElectricCar("Tesla Model 3",  200000, 5500, 150),
    )

    calc.add_car(
        calculator.Car("Range Rover", 650000, 3, 3000, 7000),
    )

    calc.add_car(
        calculator.Car("Toyota Camry", 60000, 8, 1200, 2400),
    )

calc.print_cars()


class Customer:
    def __init__(self, first_name, last_name, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_number = passport_number


class BankAccount:
    def __init__(self, number, currency):
        self.number = number
        self.currency = currency
        self.amount = 0

    def deposit(self, cash):
        self.amount += cash

    def withdraw(self, cash):
        self.amount -= cash


class Bank:
    def __init__(self):
        self.customers = {}
        self.accounts = {}

    def add_account(self, account: BankAccount, customer: Customer):
        self.accounts[customer] = account

    def add_customer(self, first_name, last_name, passport_number):
        customer = Customer(first_name, last_name, passport_number)
        self.customers[customer.passport_number] = customer  # добавляем значение по ключу

    def get_customer(self, passport_number):
        if passport_number not in self.customers:
            raise KeyError(f"Клиент с паспортом {passport_number} не найден")
        return self.customers[passport_number]

    def get_customer_account(self,passport_number):
        client = self.get_customer(passport_number)
        

bank = Bank()
bank.add_customer('Harry', 'Potter', '2128506')
customer = bank.get_customer_account('2128506')