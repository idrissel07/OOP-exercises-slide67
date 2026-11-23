"""OOP exercises: Inheritance (problems 1-3)."""


# 1. Vehicles
class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"


# 2. Person hierarchy
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, I live at {self.address}."


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)
        self.field_of_study = field_of_study

    def introduce(self):
        return f"{super().introduce()} I study {self.field_of_study}."


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return f"{super().introduce()} I work at {self.company}."


# 3. Bank accounts
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def transfer(self, destination, amount):
        """Move money to destination. False if balance is insufficient."""
        if not self.withdraw(amount):
            return False
        destination.deposit(amount)
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    # 1
    assert Vehicle().drive() == "Driving a vehicle"
    assert Car().drive() == "Driving a car"
    assert Bicycle().drive() == "Riding a bicycle"
    assert isinstance(Car(), Vehicle)
    # 2
    s = Student("Idriss", 19, "Cergy", "AI")
    e = Employee("Sara", 30, "Paris", "Enedis")
    assert s.introduce().endswith("I study AI.")
    assert e.introduce().endswith("I work at Enedis.")
    assert "Idriss" in s.introduce()
    # 3
    a = BankAccount("A1", 100)
    b = SavingsAccount("S1", 50, 0.10)
    assert a.transfer(b, 30) is True
    assert a.balance == 70 and b.balance == 80
    assert a.transfer(b, 1000) is False
    assert a.balance == 70 and b.balance == 80  # unchanged on failure
    b.add_interest()
    assert b.check_balance() == 88
    print("inheritance: all tests passed")
