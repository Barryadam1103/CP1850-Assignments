print("GREATEST COMMOM DIVISOR")

m = int(input("Enter number"))
n = int(input("Enter number"))

d = min(m,n)

while (n % d) or (m % d):
    d = d - 1

print("The Greatest Common Divisor is", d)


