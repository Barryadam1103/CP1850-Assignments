def isprime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def nextprime(number):
    while isprime(number+1) == False:
        number = number + 1
    return number+1


n = int(input('Enter a number:  '))
print(nextprime(n))