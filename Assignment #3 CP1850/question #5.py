print("NO MORE PENNIES")

pen_per_nickel = 5
nickel = 0.05
total = 0
coin = input("Enter amount (blank to quit:")

while coin !="":
    total = total + float(coin)
    coin = input("Enter amount (blank to quit:")
print("The total amount is %.02f" % total)

rounding_pennie = total * 100 % pen_per_nickel

if rounding_pennie < pen_per_nickel /2:
    cash_total = total - rounding_pennie / 100

else:
    cash_total = total + nickel -rounding_pennie / 100

print("The total amount in cash is %.02f" % cash_total)

    
        
