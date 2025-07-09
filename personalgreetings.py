def send_greeting(name):
    greeting = f"Hello, {name}! Wishing you a wonderful day! 😊"
    return greeting

# Example usage
if __name__ == "__main__":
    # You can customize the name or take it from user input
    person_name = input("Enter the name of the person: ")
    message = send_greeting(person_name)
    print(message)