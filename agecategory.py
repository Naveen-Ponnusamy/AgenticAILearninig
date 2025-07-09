def classify_age(age):
    if age < 0:
        return "Invalid age."
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

def main():
    try:
        age = int(input("Enter the age: "))
        category = classify_age(age)
        print(f"The person is a: {category}")
    except ValueError:
        print("Please enter a valid integer age.")

if __name__ == "__main__":
    main()