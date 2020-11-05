from menu import Menu


class Waiter(Menu):
    def __init__(self, customer):
        super().__init__()  # Calling the Menu's initialisation method
        self.name = "Alfred"  # Giving the waiter a name
        self.customer_name = customer  # Storing the customer's name so that we can greet them
        self.order = []  # Creating an empty list to add chosen menu items to
        self.order_price = 0  # Creating a variable to store the price of the meal
        self.finished = False  # Boolean holding whether the transaction is finished

    def greeting(self):  # Simple greetings message
        print(f"Hello {self.customer_name}, welcome to our wonderful establishment! I'm {self.name} and "
              f"I'll be helping you with your order today. \nHere is the menu we have today, there are "
              f"also special offers noted at the bottom!")
        self.display_menu()

    def display_menu(self):
        print("Menu:")  # Printing the 'Menu:' header followed by all of the items and their prices
        for items, price in self.current_menu.items():
            print(f"{items}: £{price}")
        # Requesting user input for which item they wish to purchase
        requested_item = input("If you would like to purchase an item, please type the name of the item:  ")
        # Check if the item is on the menu, if it is, add it to the order list and update the price of the meal
        for i in self.current_menu.keys():
            if i == requested_item:
                self.order.append(requested_item)
                self.order_price += float(self.current_menu[requested_item])
        self.display_order()  # Calling the display_order method
        while not self.finished:
            more = input("Would you like to buy some more food (Y/N)?  ")
            if more == "Y":
                self.display_menu()
            elif more == "N":
                print("Thank you, we will start preparing your meal now.")
                self.finished = True
            else:
                print("Please enter either 'Y' or 'N'")

    def display_order(self):  # Prints all of the selected items and the total price of the order
        print("Your current order is:")
        for _ in self.order:
            print(_)
        print(f"Order Total: {self.order_price}")


alfred = Waiter("Jen")
alfred.greeting()
