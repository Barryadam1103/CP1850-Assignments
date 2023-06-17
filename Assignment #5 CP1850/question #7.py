def removeoutliers(data, num_outliers):
    retval = sorted(data)
    
    for i in range(num_outliers):
        retval.pop()
        
    for i in range(num_outliers):
        retval.pop()
        
    return retval

def main():
    values = []
    s = input("Enter a value (blank to exit): ")
    while s != "":
        num = float(s)
        values.append(num)
        s = input("Enter a value (blank to exit): ")
        
    if len(values) < 4:
        print("Enter more values")
    else:
        print("With the outliers removed: ", removeoutliers(values, 2))
        print("The orginal data: ", values)
        
main()