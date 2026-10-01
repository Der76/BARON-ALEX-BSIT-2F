"""
user_input.py
Handles the Y/N questions asked to the customer.
"""


def ask_yes_no(prompt_text):
    """Asks a Y/N question. Returns True for Y, False for N."""
    while True:
        choice = input(prompt_text).strip().upper()

        if choice == "Y":
            return True

        if choice == "N":
            return False

        print("Invalid choice. Please enter Y or N.")


def ask_to_order():
    return ask_yes_no("\nWould you like to place an order? (Y/N): ")


def ask_another_item():
    return ask_yes_no("\nWould you like to order another item? (Y/N): ")