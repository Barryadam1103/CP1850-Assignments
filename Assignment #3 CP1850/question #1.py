print("PRIME NUMBERS'")
i = 2
n = int(input("Enter a number (number must be greater than 2:   "))
while (i!=1):
    fac = n%i
    if (fac==0):
        n =n/i
        print(i)
    
    else:
        i = i +1