print("IS A NUMBER PRIME")
n = int(input("Enter a number:  "))
def isprime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True
        
if isprime(n):
    print('Not Prime')
else:
    print('Prime')