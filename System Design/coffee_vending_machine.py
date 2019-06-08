import json

from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def coin_inserted(self):
        pass
    
    @abstractmethod
    def product_selection(self):
        pass
    
    @abstractmethod
    def dispatch(self):
        pass
    
    @abstractmethod
    def return_change(self):
        pass

class VendingMachine(ABC):
    def __init__(self):
        self._state = Idle()
        self._items = list()
        self._quantity = dict()
        self._price = dict()

    def set_items(self, items):
        self._items = items
    
    def set_quantity(self, item, quantity):
        self._quantity[item] = quantity
    
    def set_price(self, item, price):
        self._price[item] = price
    
    def insert_coin(self, denomination):
        self._state.coin_inserted(denomination)

class Idle(State):
    def coin_inserted(self, amount):
        print(f"Current Balance: {amount}")
    
    def product_selection(self):
        print("Not Allowed")
    
    def dispatch(self):
        print("Not Allowed")
    
    def return_change(self):
        print("Not Allowed")

class InsertCoin(State):
    def coin_inserted(self, amount):
        print(f"Current Balance: {amount}")
    
    def product_selection(self):
        print("Not Allowed")
    
    def dispatch(self):
        print("Not Allowed")
    
    def return_change(self):
        print("Not Allowed")

if __name__ == '__main__':
    machine = VendingMachine()
    machine.set_items(["A", "B", "C"])
    machine.set_price("A", 20)
    machine.set_price("B", 10)
    machine.set_price("C", 5)
    machine.set_quantity("A", 200)
    machine.set_quantity("B", 100)
    machine.set_quantity("C", 50)
    machine.insert_coin(10)
    

