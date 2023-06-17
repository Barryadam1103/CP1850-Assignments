def formatlist(items):
    if len(items) ==  0:
        return "<empty>"
    if len(items) == 1:
        return str(items[0])
    elif len(items) == 2:
        return str(items[0] and [1])
    elif len(items) == 3:
        return str(items[0], [1] and [2])
    elif len(items) == 4:
        return str(items [0], [1], [2] and [3])
    else:
        print("You went over the limit (4 items max!!")
    
   
    for i in range (0, len(items) - 2):
        results = results + str(items[i]) + ", "
        
        
    
    results = results + str(items[len(items) - 2]) + " and "
    results = results + str(items[len(items) - 1])
    
    return results


def main():
    items = []
    line = input("Enter an item here (blank to exit):  ")
    while line != "":
        items.append(line)
        line = input("Enter an item here (blank to exit):  ")
        
    print("The items are %s." % formatlist(items))

main()
    