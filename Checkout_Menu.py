def start(order):
    subtotal = 0
    tax_rate = 0.095
    
    print("Your order is:")
    for i in order:
        if i.quantity == 1:
            print(i.quantity, i.size, i.type, "Pizza for","$"+str(i.price))
            subtotal += i.price
        elif i.quantity >= 2:
            print(i.quantity, i.size, i.type, "Pizzas for","$"+str(i.price))
            subtotal += i.price
    subtotal = round(subtotal, 2)
    print("Subtotal: $"+str(subtotal)+"\n")
    tax = subtotal * tax_rate
    tax = round(tax, 2)
    print("Your tax is: $"+str(tax)+"\n")
    total = tax + subtotal
    total = round(total, 2)
    print("For a total of: $"+str(total))
    payment(total)
    save(order, total)
    order = []
    input("(Press Enter to Continue)")
def payment(total):
    while True:
        payment_type = input("Cash or credit? ")
        if payment_type.lower() == "cash":
            print(f"The total is ${total}.")
            cash = int(input("Enter cash received: "))
            change = cash - total
            change = round(change, 2)
            print(f"Returning ${change} to the customer")
            break
        elif payment_type.lower() == "credit":
            print(f"The total is ${total}.")
            print("Swipe your card")
            break
        else:
            print("Enter a valid response")
def save(order, total):
    with open("Pizza.dat", "a") as orders:
        for pizza in order:
            orders.write(f"{pizza.quantity} {pizza.size} {pizza.type} pizza(s) for {pizza.price}")
            orders.write("\n")
        orders.write(f"For a total of ${total} \n")