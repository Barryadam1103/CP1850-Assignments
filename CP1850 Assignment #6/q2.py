print("Shopping List Manger")

def display_menu():
    print('1. ADD-----Item To List')
    print('2. DISPLAY-----Shopping List')
    print('3. REMOVE-----Item from List')
    


def add_item(file_name):
    with open(file_name, 'a') as shoppinglist_manager:
        print("Shopping List Manger!!!")
        item = str(input("Enter Item to add to the shopping list:  "))
        price = float(input("Enter price:   "))
        quanitity = int(input("Enter amount of the item:  "))
        items = [item, price, quanitity]
        shoppinglist_manager.write(str(items) + '\n')
        
def display_shopping_list(file_name):
    with open(file_name, 'r') as shoppinglist_manager:
        for items in shoppinglist_manager:
            print(items, end='')
            
def remove_item(file_name):
    display_shopping_list(file_name)
    item_remove = str(input("Enter item you would like to remove:   "))
    remove = ''
    with open(file_name, 'r') as shoppinglist_manager:
        for items in shoppinglist_manager:
            if item_remove in items:
                continue
            else:
                remove += items
    with open(file_name, 'w') as shoppinglist_manager:
        shoppinglist_manager.write(remove)






def main():
    file = input('Enter Filename (default: shopping_list.csv):')
    if file == '':
        file = "shopping_list.csv"
    while True:
        display_menu()
        choice = input('Enter choice:   ')
        if choice == '1':
            add_item(file)
        elif choice == '2':
            display_shopping_list(file)
        elif choice == '3':
            remove_item(file)
            
        else:
            print('Invalid Choice. Try Again!!!!')

if __name__ == '__main__':
    main()
