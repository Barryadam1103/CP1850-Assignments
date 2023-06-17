print("Compound Interest")
import math


depo_amount = float(input("How much would you like to deposit:  "))
rate_interest = float(input("Enter rate of interest:  "))
num_years = float(input("Enter amount of years:  "))

i_future = depo_amount * (math.pow((1 + rate_interest / 100), num_years)) 
compound_int = i_future - depo_amount


print("Future Compound Interest for Deposited Amount {0} = {1}".format(depo_amount, i_future))
print("Compound Interest for Deposited Amount {0} = {1}".format(depo_amount, compound_int))




