def start():
    print("\nThis is the order menu, where you can view our menu and the orders we need to respond to.\n")
    print("Select an option:")
    print("1. Check Orders")
    print("2. Check Menu")
    print("3. Return to Main Menu\n")
    while True:
        selection = int(input(">> "))
        if selection == 1:
            print("1")
        elif selection == 2:
            print("2")
        elif selection == 3:
            print("\nWelcome to our Pizzaria!\n")
            print("Select an option:")
            print("1. Order")
            print("2. Checkout")
            print("3. Inventory\n")
            break
        else:
            print("Invalid Selection\n")