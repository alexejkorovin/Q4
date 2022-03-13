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

def order():
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

    ordered_item_1 = get_order(menu_items_1)
    ordered_item_2 = get_order(menu_items_2)
    ordered_item_3 = get_order(menu_items_3)
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
    print(get_reward_spin('Reward Spins ', spin_promotion(subtotal), my_round(get_gst(subtotal, GST_RATE)) + my_round(subtotal)))
    print()


def get_order(item: str):
    try:
        ordered_item_1 = int(input("Enter order for {0}: ".format(item)))
        if ordered_item_1 < 0:
            ordered_item_1 = 0
        return ordered_item_1
    except ValueError:
        return 0


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
        return my_round(total / 100 * rate+0.005)   # if3rd number after dot is 5 (ex 0.005->0.01)
    else:
        return my_round(total / 100 * rate)


def my_round(num: float) -> float:
    return int(num * 100 + 0.5) / 100


def spin_promotion(subtotal):
    if subtotal >= 30:
        spins = subtotal // 30
        return int(spins)
    else:
        return ":("


def get_reward_spin(item: str, out: str, total: float) -> str:
    if out == ":(":
        line = str("{0:<48} {1:<7}".format(item, out))
        return line
    else:
        num = int(out)
        if len(str(total)) > 5:

            spaces = len(str(int(total)))-len(str(num))+3
            line = str(f"{item:<50}"+spaces*" "+f"{num:>1.0f}")
            return line
        else:
            line = str("{0:<48} {1:>7.0f}".format(item, num))
            return line


def main():
    order()


if __name__ == "__main__":
    main()


