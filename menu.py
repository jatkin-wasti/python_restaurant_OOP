# Creating the Menu class which the Waiter class will inherit from
class Menu:
    def __init__(self):
        # Creating dictionaries with item names and their prices
        self.food = {"Burger": 5.00, "Chips": 2.00}
        self.drinks = {"Coca Cola": 0.99, "Fanta": 0.99, "Coffee": 2.00, "Tea": 1.50}
        self.special_offers = {"Special Burger": 9.00}


menu = Menu()  # Creating an instance of the Menu class
