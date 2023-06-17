print("SHIPPING CALCULATOR")
base_amount = 10.95

def shipping_total(items):
    total = base_amount + (items * 2.95)
    return total

items_amount = int(input("Enter the amount of items:  "))
items_amount -=1
total_amount = shipping_total(items_amount)
print("Your total is", (round(total_amount, 2)))
