def count_range(a_list, minimum, maximum):
    count = 0
    for number in a_list:
        if minimum <= number < maximum:
            count += 1       
    return count


my_list = [5,2,8,9,3,1,7]
print(count_range(my_list, 3, 8))