""" This Module is the Main Module """
import sys
from inventory_management import MarketPrices
from inventory_management import InventoryClass
from inventory_management import FurnitureClass
from inventory_management import ElectricAppliancesClass

FULL_INVENTORY = {}


def main_menu(user_prompt=None):
    """
    Queries Users for Main Menu Options
    :param user_prompt: User Option Prompt
    :return: User's Response to Prompt
    """
    valid_prompts = {"1": add_new_item,
                     "2": item_info,
                     "q": exit_program}
    options = list(valid_prompts.keys())

    while user_prompt not in valid_prompts:
        options_str = ("{}" + (", {}") * (len(options)-1)).format(*options)
        print("Please choose from the following options ({}):"
              .format(options_str))
        print("1. Add a new item to the inventory")
        print("2. Get item information")
        print("q. Quit")
        user_prompt = input(">")
    return valid_prompts.get(user_prompt)


def get_price():
    """
    Prints 'Get Price' to the screen
    :return: None
    """
    print("Get price")


def add_new_item():
    """
    :return: Appends current Dictionary w/ New Item
    """

    item_code = input("Enter item code: ")
    item_description = input("Enter item description: ")
    item_rental_price = input("Enter item rental price: ")

    # Get price from the market prices module
    item_price = MarketPrices.get_latest_price()

    is_furniture = input("Is this item a piece of furniture? (Y/N): ")
    if is_furniture.lower() == "y":
        item_material = input("Enter item material: ")
        item_size = input("Enter item size (S,M,L,XL): ")
        new_item = FurnitureClass.Furniture(item_code,
                                            item_description,
                                            item_price,
                                            item_rental_price,
                                            item_material,
                                            item_size)
    else:
        is_electric_appliance = \
            input("Is this item an electric appliance? (Y/N): ")
        if is_electric_appliance.lower() == "y":
            item_brand = input("Enter item brand: ")
            item_voltage = input("Enter item voltage: ")
            new_item = ElectricAppliancesClass.ElectricAppliances(
                item_code,
                item_description,
                item_price,
                item_rental_price,
                item_brand,
                item_voltage)
        else:
            new_item = InventoryClass.Inventory(item_code,
                                                item_description,
                                                item_price,
                                                item_rental_price)
    FULL_INVENTORY[item_code] = new_item.return_as_dictionary()
    print("New inventory item added")


def item_info():
    """
    Prints the Item to screen based on code
    :return: None
    """
    item_code = input("Enter item code: ")
    if item_code in FULL_INVENTORY:
        print_dict = FULL_INVENTORY[item_code]
        for key, value in print_dict.items():
            print("{}:{}".format(key, value))
    else:
        print("Item not found in inventory")


def exit_program():
    """
    Exits program
    :return: None
    """
    sys.exit()


if __name__ == '__main__':
    while True:
        print(FULL_INVENTORY)
        main_menu()()
        input("Press Enter to continue...........")
