print("Day Old Bread")

# Ask user for number of bread
day_old_bread = int(input("How many Loafs of bread would you like to buy?  "))

# Calculate price of bread
regular_bread = day_old_bread * 3.49
discounted_bread = regular_bread * 0.6
day_old_bread_price = regular_bread - discounted_bread

#print results
print("The Regular price of the bread is", round(regular_bread, 2))
print("The discounted of the bread is", round(discounted_bread, 2))
print("The total price is", round(day_old_bread_price, 2))





