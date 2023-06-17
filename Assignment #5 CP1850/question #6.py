numbers = []
while True:
    num = input("Enter a number:  ")
    if num =="":
        break
    numbers.append(num)
print('Original List:',numbers)

# List Reverse
numbers.reverse()

# updated list
print('Updated List:', numbers)