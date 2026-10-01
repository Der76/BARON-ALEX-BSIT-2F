"""
calculations.py
Handles the subtotal and discount computations.
"""

from config import (DISCOUNT_TIER_1_AMOUNT, DISCOUNT_TIER_1_RATE,
                    DISCOUNT_TIER_2_AMOUNT, DISCOUNT_TIER_2_RATE)


def calculate_subtotal(orders):
    subtotal = 0

    for order in orders:
        subtotal += order["total"]

    return subtotal


def calculate_discount(subtotal):
    if subtotal >= DISCOUNT_TIER_1_AMOUNT:
        discount_rate = DISCOUNT_TIER_1_RATE
    elif subtotal >= DISCOUNT_TIER_2_AMOUNT:
        discount_rate = DISCOUNT_TIER_2_RATE
    else:
        discount_rate = 0

    discount_amount = subtotal * discount_rate
    total_amount = subtotal - discount_amount

    return discount_amount, discount_rate, total_amount