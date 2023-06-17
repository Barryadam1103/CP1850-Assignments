print("Party List Program")

def display_menu():
    print('1. ADD guest to party list')
    print('2. DISPLAY party list')
    print('3. REMOVE guest from party list')
    print('4. LIST the total number of guests')


def add_guest(file_name):
    with open(file_name, 'a') as partylist_manager:
        print("WELCOME TO THE PARTY!!")
        name = str(input("Hello what is your name?:  "))
        guest = (name)
        partylist_manager.write(str(guest) + '\n')
        
def display_party_list(file_name):
    with open(file_name, 'r') as partylist_manager:
        for guest in partylist_manager:
            print(guest, end='')
            
def remove_guest(file_name):
    display_party_list(file_name)
    name_remove = str(input("Enter name you would like to remove:   "))
    remove = ''
    with open(file_name, 'r') as partylist_manager:
        for guest in partylist_manager:
            if name_remove in guest:
                continue
            else:
                remove += guest
    with open(file_name, 'w') as partylist_manager:
        partylist_manager.write(remove)






def main():
    file = input('Enter Filename (default: party_list.txt):')
    if file == '':
        file = "party_list.txt"
    while True:
        display_menu()
        choice = input('Enter choice:   ')
        if choice == '1':
            add_guest(file)
        elif choice == '2':
            display_party_list(file)
        elif choice == '3':
            remove_guest(file)
            
        else:
            print('Invalid Choice. Try Again!!!!')

if __name__ == '__main__':
    main()





        
    
        


        
        
    


    
    