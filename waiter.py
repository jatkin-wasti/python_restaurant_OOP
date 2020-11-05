from menu import Menu


class Waiter(Menu):
    def __init__(self, customer):
        super().__init__()
        self.name = "Alfred"
        self.customer_name = customer
        self.order = []
        self.order_price = 0
        self.finished = False

    def greeting(self):
        print(f"Hello {self.customer_name}, welcome to our wonderful establishment! I'm {self.name} and "
              f"I'll be helping you with your order today. \nHere is the menu we have today, there are "
              f"also special offers noted at the bottom!")
        self.display_menu()

    def display_menu(self):
        print("Menu:")
        for items, price in self.current_menu.items():
            print(f"{items}: £{price}")
        requested_item = input("If you would like to purchase an item, please type the name of the item:  ")
        for i in self.current_menu.keys():
            if i == requested_item:
                self.order.append(requested_item)
                self.order_price += float(self.current_menu[requested_item])
        self.display_order()
        while not self.finished:
            more = input("Would you like to buy some more food (Y/N)?  ")
            if more == "Y":
                self.display_menu()
            elif more == "N":
                print("Thank you, we will start preparing your meal now.")
                self.finished = True
            else:
                print("Please enter either 'Y' or 'N'")


    def display_order(self):
        print("Your current order is:")
        for _ in self.order:
            print(_)
        print(f"Order Total: {self.order_price}")


alfred = Waiter("Jen")
alfred.greeting()
