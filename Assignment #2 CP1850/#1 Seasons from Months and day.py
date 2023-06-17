print("SEASONS FROM MONTH TO DAY!")

# Get User Input
month = input("Enter month:   ")
day = int(input("Enter day:   "))


if month in ('december', 'january', 'feburary', 'march'):
    season = 'winter'
elif month in ('april', 'may', 'june'):
    season = 'spring'    
elif month in ('july', 'august', 'september'):
    season = 'summer'
else:
    season = 'fall'
    

if (month == 'march') and (day > 19):
    season = 'spring'    
elif (month == 'june') and (day > 20):
    season = 'summer'    
elif (month == 'september') and (day > 21):
    season = 'fall'
elif (month == 'winter') and (day > 20):
    season = 'winter'
# Get Results    
print("The Season is", season)
    

    
    


