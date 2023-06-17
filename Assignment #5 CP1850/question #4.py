num_a = []
lower = []
higher = []


while True:
    choice_i =input("Would you like to enter a number:(y/n)")
    if choice_i.lower() == "y":
        num=int(input("Enter Number:"))
        num_a.append(num)
        
    else:
        summation = sum(num_a)
        length = len(num_a)
        average = round(summation/length,0)
        
        
        for num in num_a:
            if num < average:
                lower.append(num)
            
            else:
                higher.append(num)
                
        
        print("The Average of the numbers is",average)
        print("The lower then averages are",lower)
        print("The higher then averages are",higher)
        break