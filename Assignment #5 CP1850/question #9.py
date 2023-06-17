def sort_list(num):
    n = len(num)
    if n == 1 or n == 0:
        return True

    return num[0] <= num[1] and sort_list(num[1:])
 
 
num = [20, 21, 23, 24, 78, 88]
 
# Displaying result
if sort_list(num):
    print("Yes the list is sorted")
else:
    print("No the list isn't sorted")