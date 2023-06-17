print("Wind Chill")
# Get user input
wind_chill = float(input("What is the Wind speed:  "))
air_temp = float(input("What is the Air Temperature:  "))

#calculate wci
wci=round(13.12 + 0.6215*air_temp-11.37*wind_chill**0.16+0.39*air_temp*wind_chill**0.16)

#print results
print("The wind chill is: ", wci, "degrees")
       