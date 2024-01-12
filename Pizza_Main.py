"""
Title: Pizza Time
Description: A pizzaria simulator
Author: Why would I want to claim responsibility for the this?
"""

import Order_Menu
import Checkout_Menu
import Inventory_Menu
def start():
    print("\nWelcome to our Pizzaria!\n")
    print("Select an option:")
    print("1. Order")
    print("2. Checkout")
    print("3. Inventory\n")
    while True:
        selection = int(input(">> "))
        if selection == 0:
            print("\nWelcome to our Pizzaria!\n")
            print("Select an option:")
            print("1. Order")
            print("2. Checkout")
            print("3. Inventory\n")
            print("4. Exit")
        elif selection == 1:
            Order_Menu.start()
        elif selection == 2:
            Checkout_Menu.start()
        elif selection == 3:
            Inventory_Menu.start()
        elif selection == 4:
            print("Hope we see you soon!")
            break
        else:
            print("Invalid Selection\n")
start()