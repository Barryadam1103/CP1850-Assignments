print("Print All Prime Numbers")

Number = 1

while(Number <= 100):
    count = 0
    i = 2
    # Shows all numbers that are prime within 100
    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
# User gets the prime factors        
        print(" %d" %Number, end = '  ')
    Number = Number  + 1