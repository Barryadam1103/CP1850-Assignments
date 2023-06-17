print("Making Change")
change = int(input("Enter Amount:  "))
#Get user input

toonies = change // 200
loonies = (change - toonies*200) // 100
quarters = (change - toonies*200 - loonies*100) // 25
dimes = (change - toonies*200 - loonies*100 - quarters*25) // 10
nickels = (change - toonies*200 - loonies*100 - quarters*25 - dimes*10) // 5
pennies = (change - toonies*200 - loonies*100 - quarters*25 - dimes*10 - nickels*5) // 1


# Get results
print('The change you will be getting back', toonies, 'toonies,', loonies, 'loonies',\
      quarters, 'quarters,', dimes, 'dimes,', nickels, 'nickels')





