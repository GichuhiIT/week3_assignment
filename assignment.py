# Week 3 Assignment

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Only applies the discount if discount_percent is 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price


# Ask user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    print(f"Final price: {final_price}")
except ValueError:
    print("Invalid input. Please enter numeric values only.")
