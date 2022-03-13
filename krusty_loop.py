'''
    Author: Alexey Korovin
    SID: 520190377
    Unikey: akor6986
'''
# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the following lines of code
# have been copied and modified from my own work Q3 - Functions

from krusty import new_customer

def loop_krusty():
    is_order = "y"
    counter = 0
    check = True # krusty_loop breaks loop and returns number of customers when new_customer returns False (check)
    while (is_order == "Y" or is_order == "y") and (check == True):
        if check == False:
            print("****************")
            print("Total Orders: {0}".format(counter))
            print("****************")
            break
        is_order = input("New Order[Y/N]: ")
        if is_order == "n" or is_order == "N":
            print("****************")
            print("Total Orders: {0}".format(counter))
            print("****************")
            break
        if is_order == "y" or is_order == "Y":
            check = new_customer()
            if check == False:
                break
            counter += 1
        else:
            is_order = "y"
            continue

    #need to check all conditions for n N y Y and ither values

def main():
    loop_krusty()


if __name__ == "__main__":
    main()
