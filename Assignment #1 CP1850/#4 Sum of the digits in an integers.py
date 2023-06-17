print("Sum of the digits in an Integer")

#ask user for 4 numbers
sum_of_digts = int(input("Enter 4 Number Here:    "))


number_one = sum_of_digts // 1000
number_two = sum_of_digts % 1000 // 100
number_three = sum_of_digts % 100 //10
number_four = sum_of_digts % 10 / 1
total_num = number_one + number_two + number_three + number_four

#print results
print(number_one,"+",number_two,"+",number_three,"+",number_four,"=",total_num)






