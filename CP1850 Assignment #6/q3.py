import pickle
def display_menu():
    print('1. ADD item')
    print('2. DISPLAY iventory')
    print('3. REMOVE item')
    print('4. Exit')


def add_item(file_name):
    with open(file_name, 'a') as petstore_manager:
        print("WELCOME TO THE PET IVENTORY")
        name = str(input("Enter Item:  "))
        price = float(input("Enter price:  "))
        quantity = int(input("Enter amount left:  "))
        item = [name, price, quantity]
        petstore_manager.write(str(item) + '\n')
        
def display_inventory(file_name):
    with open(file_name, 'r') as petstore_manager:
        for item in petstore_manager:
            print(item, end='')
            
def remove_item(file_name):
    display_inventory(file_name)
    name_remove = str(input("Enter item you would like to remove:   "))
    remove = ''
    with open(file_name, 'r') as petstore_manager:
        for item in petstore_manager:
            if name_remove in item:
                continue
            else:
                remove += item
    with open(file_name, 'w') as petstore_manager:
        petstore_manager.write(remove)


def main():
    file = input('Enter Filename (default: petstore.bin):')
    if file == '':
        file = "petstore.bin"
    while True:
        display_menu()
        choice = input('Enter choice:   ')
        if choice == '1':
            add_item(file)
        elif choice == '2':
            display_inventory(file)
        elif choice == '3':
            remove_item(file)
        elif choice =='4':
            break
            
        else:
            print('Invalid Choice. Try Again!!!!')

if __name__ == '__main__':
    main()
