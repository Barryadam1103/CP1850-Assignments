print ("THE RICHTER SCALE!")

# Get user input
magnitude = float(input("Enter the magnitude of the earthquake"))

if magnitude < 2.0:
    descriptor = 'Mirco'
elif magnitude < 3.0:
    descriptor = 'Very Minor'
elif magnitude < 4.0:
    descriptor = 'Minor'
elif magnitude < 5.0:
    decriptor = 'Light'
elif magnitude < 6.0:
    descriptor = 'Moderate'
elif magnitude < 7.0:
    descriptor = 'Strong'
elif magnitude < 8.0:
    descriptor = 'Major'
elif magnitude < 10:
    descriptor = 'Great'
elif magnitude > 10:
    descriptor = 'Meteoric'
    
# Get results
print("The Descriptor of the earthquake is", descriptor)
