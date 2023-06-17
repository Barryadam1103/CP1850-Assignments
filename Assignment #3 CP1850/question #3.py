num = 0
while True:
    additionals = input("Are there additional guests? \n press Enter for yes \nPress space for no and then enter \n")
    if additionals == (" "):
        print("Cost is $", round(num, 2))
        break
    age = int(input("Enter your age"))
    if age <= 2:
        num = num + 0
    elif age >= 3 and age <= 12:
        num = num + 14.00
    elif age >= 65:
        num = num + 18.00
    else:
        num = num + 23.00
        