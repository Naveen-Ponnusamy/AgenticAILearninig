def calculate_total_cost(prices, tax_percent):
    subtotal = sum(prices)
    tax_amount = subtotal * (tax_percent / 100)
    total = subtotal + tax_amount
    return subtotal, tax_amount, total

def main():
    try:
        print("Enter the prices of 3 items:")
        item1 = float(input("Item 1: ₹"))
        item2 = float(input("Item 2: ₹"))
        item3 = float(input("Item 3: ₹"))
        tax = float(input("Enter tax percentage: "))

        prices = [item1, item2, item3]
        subtotal, tax_amount, total = calculate_total_cost(prices, tax)

        print("\n--- Bill Summary ---")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax ({tax}%): ₹{tax_amount:.2f}")
        print(f"Total Cost: ₹{total:.2f}")
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()