"""
order.py
Class      = QuickBiteOrder (the blueprint)
Attributes = menu, orders, subtotal, discount_rate,
             discount_amount, total_amount
Methods    = display_header, display_menu, ask_to_order, take_order,
             calculate_subtotal, calculate_discount,
             display_receipt, display_exit_message
"""


class QuickBiteOrder:
    DISCOUNT_TIER_1_AMOUNT = 1000
    DISCOUNT_TIER_1_RATE = 0.10
    DISCOUNT_TIER_2_AMOUNT = 500
    DISCOUNT_TIER_2_RATE = 0.05

    # ------------------------------------------------
    # Initializer: creates the attributes of the object
    # ------------------------------------------------
    def __init__(self, menu):
        self.menu = menu
        self.orders = []
        self.subtotal = 0
        self.discount_rate = 0
        self.discount_amount = 0
        self.total_amount = 0

    # ------------------------------------------------
    # Display methods
    # ------------------------------------------------
    def display_header(self):
        print("=" * 60)
        print("                 QUICK BITE")
        print("              FAST FOOD RESTAURANT")
        print("=" * 60)

    def display_menu(self):
        print("\n" + "-" * 60)
        print("                         MENU")
        print("-" * 60)
        print(f"{'NO.':<6}{'ITEM':<32}{'PRICE':>10}")
        print("-" * 60)

        for number, item in self.menu.items():
            print(f"{number:<6}{item['name']:<32}₱{item['price']:>8.2f}")

        print("-" * 60)

    def display_receipt(self):
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

        for order in self.orders:
            print(
                f"{order['name']:<28}"
                f"{order['quantity']:>6}"
                f"₱{order['price']:>12.2f}"
                f"₱{order['total']:>12.2f}"
            )

        print("-" * 68)
        print(f"{'SUBTOTAL':<54}₱{self.subtotal:>11.2f}")
        print(
            f"{'DISCOUNT (' + str(int(self.discount_rate * 100)) + '%)':<54}"
            f"₱{self.discount_amount:>11.2f}"
        )
        print(f"{'TOTAL AMOUNT':<54}₱{self.total_amount:>11.2f}")
        print("=" * 68)
        print("                 THANK YOU!")
        print("              PLEASE COME AGAIN!")
        print("=" * 68)

    def display_exit_message(self):
        print("\n" + "=" * 60)
        print("       Thank you for visiting Quick Bite!")
        print("                  Goodbye!")
        print("=" * 60)

    # ------------------------------------------------
    # Input methods
    # ------------------------------------------------
    def ask_yes_no(self, prompt_text):
        while True:
            choice = input(prompt_text).strip().upper()

            if choice == "Y":
                return True

            if choice == "N":
                return False

            print("Invalid choice. Please enter Y or N.")

    def ask_to_order(self):
        return self.ask_yes_no("\nWould you like to place an order? (Y/N): ")

    def take_order(self):
        while True:
            try:
                item_number = int(input("\nEnter menu item number: "))

                if item_number not in self.menu:
                    print("Invalid item number. Please choose from the menu.")
                    continue

                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                item_name = self.menu[item_number]["name"]
                item_price = self.menu[item_number]["price"]
                item_total = item_price * quantity

                self.orders.append({
                    "name": item_name,
                    "quantity": quantity,
                    "price": item_price,
                    "total": item_total
                })

                print("\nOrder added successfully!")
                print(f"{item_name} x {quantity} = ₱{item_total:.2f}")

                if not self.ask_yes_no(
                    "\nWould you like to order another item? (Y/N): "
                ):
                    return

            except ValueError:
                print("Invalid input. Please enter numbers only.")

    # ------------------------------------------------
    # Calculation methods
    # ------------------------------------------------
    def calculate_subtotal(self):
        self.subtotal = 0

        for order in self.orders:
            self.subtotal += order["total"]

        return self.subtotal

    def calculate_discount(self):
        if self.subtotal >= self.DISCOUNT_TIER_1_AMOUNT:
            self.discount_rate = self.DISCOUNT_TIER_1_RATE
        elif self.subtotal >= self.DISCOUNT_TIER_2_AMOUNT:
            self.discount_rate = self.DISCOUNT_TIER_2_RATE
        else:
            self.discount_rate = 0

        self.discount_amount = self.subtotal * self.discount_rate
        self.total_amount = self.subtotal - self.discount_amount