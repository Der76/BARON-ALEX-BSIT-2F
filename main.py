# ============================================================
# PRELIM PERFORMANCE TASK
# RESTAURANT ORDERING SYSTEM - Python OOP Version
# ============================================================

from order import QuickBiteOrder

# Menu stored in a dictionary
MENU = {
    1: {"name": "Cheeseburger", "price": 75.00},
    2: {"name": "Chicken Burger", "price": 85.00},
    3: {"name": "Chickenjoy Meal", "price": 120.00},
    4: {"name": "Burger Steak Meal", "price": 110.00},
    5: {"name": "Spaghetti", "price": 80.00},
    6: {"name": "Carbonara", "price": 95.00},
    7: {"name": "Chicken Nuggets", "price": 70.00},
    8: {"name": "French Fries", "price": 50.00},
    9: {"name": "Onion Rings", "price": 55.00},
    10: {"name": "Chocolate Sundae", "price": 45.00},
    11: {"name": "Apple Pie", "price": 50.00},
    12: {"name": "Iced Tea", "price": 40.00},
    13: {"name": "Soft Drink", "price": 35.00},
    14: {"name": "Orange Juice", "price": 45.00},
    15: {"name": "Mineral Water", "price": 25.00}
}


def main():
    # order1 is the object (an instance of the QuickBiteOrder class)
    order1 = QuickBiteOrder(MENU)

    order1.display_header()
    order1.display_menu()

    if not order1.ask_to_order():
        order1.display_exit_message()
        return

    order1.take_order()

    if len(order1.orders) == 0:
        print("\nNo items were ordered.")
        order1.display_exit_message()
        return

    order1.calculate_subtotal()
    order1.calculate_discount()
    order1.display_receipt()


if __name__ == "__main__":
    main()