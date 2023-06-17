my_list= []
none_dup = []


while True:
    user_inp = input("Enter a word here (blank to exit):")
    if user_inp == "":
        for item in my_list:
            if item not in none_dup:
                none_dup.append(item)
        print(none_dup)
        break
    
    else:
        my_list.append(user_inp)