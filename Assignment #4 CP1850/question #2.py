print("TAXI FARE")
def distance_travelled(distance):
    distance = (distance * 1000) / 140
    fare = 4.00 + (distance * 0.25)
    return fare



distance_in_km = float(input("Enter distance in Km:  "))
total_fare = distance_travelled(distance_in_km)
print("The total taxi fare is", (round(total_fare)))
    
    
    
    
    
    
    
    
    
    
    
    

