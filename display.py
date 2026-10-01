"""
display.py
Handles everything that is printed on the screen.
"""


def display_header():
    print("=" * 60)
    print("                 QUICK BITE")
    print("              FAST FOOD RESTAURANT")
    print("=" * 60)


def display_menu(menu):
    print("\n" + "-" * 60)
    print("                         MENU")
    print("-" * 60)
    print(f"{'NO.':<6}{'ITEM':<32}{'PRICE':>10}")
    print("-" * 60)

    for number, item in menu.items():
        print(f"{number:<6}{item['name']:<32}₱{item['price']:>8.2f}")

    print("-" * 60)


def display_receipt(orders, subtotal, discount, discount_rate, total):
    print("\n")
    print("=" * 68)
    print("                    QUICK BITE")
    print("                 FAST FOOD RESTAURANT")
    print("                    OFFICIAL RECEIPT")
    print("=" * 68)

    print("Address: Cebu City, Philippines")
    print("Thank you for dining with us!")
    print("-" * 68)

    print(f"{'ITEM':<28}{'QTY':>6}{'PRICE':>14}{'TOTAL':>14}")
    print("-" * 68)

    for order in orders:
        print(
            f"{order['name']:<28}"
            f"{order['quantity']:>6}"
            f"₱{order['price']:>12.2f}"
            f"₱{order['total']:>12.2f}"
        )

    print("-" * 68)
    print(f"{'SUBTOTAL':<54}₱{subtotal:>11.2f}")
    print(
        f"{'DISCOUNT (' + str(int(discount_rate * 100)) + '%)':<54}"
        f"₱{discount:>11.2f}"
    )
    print(f"{'TOTAL AMOUNT':<54}₱{total:>11.2f}")
    print("=" * 68)
    print("                 THANK YOU!")
    print("              PLEASE COME AGAIN!")
    print("=" * 68)


def display_exit_message():
    print("\n" + "=" * 60)
    print("       Thank you for visiting Quick Bite!")
    print("                  Goodbye!")
    print("=" * 60)