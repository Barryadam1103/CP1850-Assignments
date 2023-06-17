negative = []
zeros = []
positive = []

line = input("Enter a number here:  ")

while line != "":
    num = int(line)
    
    if num < 0:
        negative.append(num)
        
    elif  num > 0:
        positive.append(num)
        
    else:
        zeros.append(num)
        
    
    line = input("Enter a number here:  ")