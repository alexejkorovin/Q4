'''
    Author: Alexey Korovin
    SID: 520190377
    Unikey: akor6986
'''


# USYD CODE CITATION ACKNOWLEDGEMENT
# I declare that the following lines of code
# have been copied from my own work Q3 - Functions
# spin_promotion function is a new function (written by myself)
# in this  code as been asked in the task


def get_order(item: str, cont_prompt: bool):
    t = input("Enter order for {0}: ".format(item))  #
    if t == "n" or t == "N":  # check input for N and n and if true return False to new_customer()
        cont_prompt = False
        return 0
    else:
        cont_prompt = True
        return int(t)


def get_menu(item: str, price: float) -> str:
    menu_line = str("{0:<48} ${1:>5.2f}".format(item, price))
    return menu_line


def get_summary(item: str, price: float, quantity: int) -> str:
    summary_line = str("{0:<48} ${1:>6.2f} x {2:>2}".format(item, price, quantity))
    return summary_line


def get_summary_bill(item: str, total: float) -> str:
    subtotal_line = str("{0:<48} ${1:>6.2f}".format(item, total))
    return subtotal_line


def get_subtotal(price: float, quantity: int) -> float:
    subtotal = price * quantity
    return subtotal


def get_gst(total: float, rate: int) -> float:
    if int((total / 100 * rate) * 1000 % 10) == 5:  # round up to 3 decimals
        return my_round(total / 100 * rate + 0.005)  # if3rd number after dot is 5 (ex 0.005->0.01)
    else:
        return my_round(total / 100 * rate)


def my_round(num: float) -> float:
    return int(num * 100 + 0.5) / 100


def new_customer():
    menu_items_1 = "Krusty Burger"
    menu_items_2 = "Milkshake"
    menu_items_3 = "Krusty Meal Set[Burger + Drink + Krusty Laugh]"
    menu_price_1 = 5.10
    menu_price_2 = 3.50
    menu_price_3 = 10.50
    GST_RATE = 5

    print("Welcome to Krusty Burgers!")
    print(get_menu(menu_items_1, menu_price_1))
    print(get_menu(menu_items_2, menu_price_2))
    print(get_menu(menu_items_3, menu_price_3))
    print()

    # if prompt of the customer was sucessfull (input was not n or N) continue iterate over menu
    # and if prompt was not sucessfull (input was n or N) return False to loop function in krusty_loop.py
    # krusty_loop breaks loop and returns number of customers when new_customer returns False
    cont_prompt = True
    if cont_prompt:
        ordered_item_1 = get_order(menu_items_1, cont_prompt)
    if cont_prompt:
        ordered_item_2 = get_order(menu_items_2, cont_prompt)
    if cont_prompt:
        ordered_item_3 = get_order(menu_items_3, cont_prompt)
    else:
        return False

    print()
    print("Order Summary")
    print(get_summary(menu_items_1, menu_price_1, ordered_item_1))
    print(get_summary(menu_items_2, menu_price_2, ordered_item_2))
    print(get_summary(menu_items_3, menu_price_3, ordered_item_3))

    subtotal = get_subtotal(menu_price_1, ordered_item_1) + get_subtotal(menu_price_2, ordered_item_2) + \
               get_subtotal(menu_price_3, ordered_item_3)

    print(get_summary_bill('Sub-total', subtotal))
    print(get_summary_bill('GST', get_gst(subtotal, GST_RATE)))
    print(get_summary_bill('Total', my_round(get_gst(subtotal, GST_RATE)) + my_round(subtotal)))
    print()
    return True


def main():
    new_customer()


if __name__ == "__main__":
    main()
