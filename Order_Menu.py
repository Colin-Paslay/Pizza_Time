import warnings, pandas

class Order:
    def __init__(self, size, type, quantity, price):
        self.size = size
        self.type = type
        self.quantity = quantity
        self.price = price

warnings.simplefilter(action='ignore', category=FutureWarning)

def start():
    order = []
    pizza_menu = pandas.read_csv("data/types.csv")
    print(pizza_menu[["Type", "Size", "Price"]])
    while True:
        print("\nWhat kind of pizza do you want?\n")   
        selection = int(input(">> "))
        if selection > len(pizza_menu)-1 or selection < 0:
            print("Invalid selection")
            continue
        size = pizza_menu.loc[selection][1]
        ptype = pizza_menu.loc[selection][0]
        quantity = int(input(f"How many {size} {ptype} Pizzas would you like? "))
        price = pizza_menu.loc[selection][2] * quantity
        if quantity >= 1:
            order.append(Order(size, ptype, quantity, price))
        else: 
            continue
        print("Add another type of pizza? (Y/N)")
        yn = input(">> ")
        if yn.lower() == "y":
            continue
        else:
            break
    for i in order:
        if i.quantity == 1:
            print(i.quantity, i.size, i.type, "Pizza for","$"+str(i.price))
        elif i.quantity >= 2:
            print(i.quantity, i.size, i.type, "Pizzas for","$"+str(i.price))
    return order