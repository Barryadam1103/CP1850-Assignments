print("Sort Three Integers")
# User Gives Three Integers
int_1 = float(input("Enter a number:  "))
int_2 = float(input("Enter a number:  "))
int_3 = float(input("Enter a number:  "))

#caluclate the lowest middle and highest numbers
lowest = min(int_1,int_2,int_3)
highest = max(int_1,int_2,int_3)
middle = sum([int_1,int_2,int_3])-highest-lowest

#get results
print("The order of the integers are:  ", lowest,middle,highest)



