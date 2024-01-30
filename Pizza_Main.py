"""
Title: Pizza Time
Description: A pizzaria simulator
Author: Why would I want to claim responsibility for the this?
"""

import Order_Menu, Checkout_Menu, Inventory_Menu
from os import system
order = []
while True:
    system('cls')
    print("\nWelcome to our Pizzaria!\n")
    print("Select an option:")
    print("1. Order")
    print("2. Checkout")
    print("3. Exit\n")
    selection = int(input(">> "))
    if selection == 1:
        order = Order_Menu.start()
    elif selection == 2:
        if len(order) > 0:
            Checkout_Menu.start(order)
        else:
            print("Please order something before chechout")
    elif selection == 3:
        print("Hope we see you soon!")
        break
    else:
        print("Invalid Selection\n")
        input("(Press Enter to Continue)")