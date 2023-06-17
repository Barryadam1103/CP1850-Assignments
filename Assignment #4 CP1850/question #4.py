print("IS IT A VALID TRAINGLE")

def valid_tri(len_1, len_2, len_3):
    if (len_1+len_2>len_3 and len_1+len_3>len_2 and len_2+len_3>len_1):
        return False
    else:
        return True

a = int(input("Enter number:  "))
b = int(input("Enter number:  "))
c= int(input("Enter number:  "))

traingle = valid_tri(a,b,c)

if (traingle ==1):
    print("Not a valid traingle")
else:
    print("Valid Traingle")
