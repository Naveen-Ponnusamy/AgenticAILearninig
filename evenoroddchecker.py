def check_odd_even(number):
    return "Even" if number % 2 == 0 else "Odd"

def main():
    # Check a single number
    try:
        num = int(input("Enter a number to check (Odd/Even): "))
        print(f"{num} is {check_odd_even(num)}.")
    except ValueError:
        print("Please enter a valid integer.")

    # Check a list of numbers
    try:
        numbers = input("\nEnter a list of numbers separated by spaces: ")
        num_list = list(map(int, numbers.split()))
        print("\nResults:")
        for n in num_list:
            print(f"{n} is {check_odd_even(n)}.")
    except ValueError:
        print("Invalid list. Make sure all inputs are integers.")

if __name__ == "__main__":
    main()