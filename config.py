"""
config.py
Stores the menu and the constants used by the program.
"""

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

# Discount rules: subtotal at or above the amount gets the rate
DISCOUNT_TIER_1_AMOUNT = 1000
DISCOUNT_TIER_1_RATE = 0.10
DISCOUNT_TIER_2_AMOUNT = 500
DISCOUNT_TIER_2_RATE = 0.05