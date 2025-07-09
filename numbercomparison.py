def compare_numbers():
    """
    Compares two numbers provided by the user and clearly states which is larger,
    which is smaller, or if they are equal.
    """
    try:
        # Get the first number from the user
        num1_str = input("Please enter the first number: ")
        num1 = float(num1_str) # Convert the input to a float to handle decimals

        # Get the second number from the user
        num2_str = input("Please enter the second number: ")
        num2 = float(num2_str) # Convert the input to a float

        # Compare the two numbers and print all three relationships
        if num1 > num2:
            print(f"The first number ({num1}) is larger than the second number ({num2}).")
            print(f"The second number ({num2}) is smaller than the first number ({num1}).")
            print(f"The numbers are not equal.")
        elif num1 < num2:
            print(f"The first number ({num1}) is smaller than the second number ({num2}).")
            print(f"The second number ({num2}) is larger than the first number ({num1}).")
            print(f"The numbers are not equal.")
        else: # num1 == num2
            print(f"The first number ({num1}) is equal to the second number ({num2}).")
            print(f"Neither number is larger or smaller than the other.")

    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to start the comparison
compare_numbers()