print("Volume of a Cylinder")
pie = 3.14
#take the radius from the user
r = float(input("What is the Radius of the cylinder:  "))

# take the height from the user
h = float(input("What is the Height of the cylinder:  "))

#calculate the volume of cylinder
volume = pie * r **2 * h

# Surface Area of a cylinder
s_area = 2* 3.14 *pow(r,2)*h

#Print Results
print("The volume of the cylinder is:", round(volume, 1))
print("The surface area of the cylinder is:", round(s_area, 1))











          