print("COMPUTE THE HYPOTENUSE")
def get_hypotenuse(side_1, side_2):
    total_hypo = (side_1 ** 2 + side_2 ** 2)** 0.5
    return total_hypo
    """    
    This Function takes side_1 and side_2 and computes the hypotenuse from the users inputs
        
    """    
def main():
    side_1 = float(input("Enter value for side 1:  "))
    side_2 = float(input("Enter valude for side 2:  "))
    
    side_3 = get_hypotenuse(side_1, side_2)
    print("The Hypotenuse is", side_3)
      
if __name__ == '__main__':
    main()