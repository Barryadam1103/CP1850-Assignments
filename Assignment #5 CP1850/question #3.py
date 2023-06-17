from random import randrange

min_num = 1
max_num = 49
num_number = 6

ticket_num = []

for i in range(num_number):
    rand = randrange(min_num, max_num + 1)
    while rand in ticket_num:
        rand = randrange(min_num, max_num + 1)
        
    ticket_num.append(rand)
    
ticket_num.sort()
print("Your numbers are: ", end="")
for n in ticket_num:
    print(n, end=" ")
    print()