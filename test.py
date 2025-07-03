def arithmetic_operators():
    print("=== Arithmetic Operators ===")
    a, b = 10, 3
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a % b = {a % b}")
    print(f"a ** b = {a ** b}")
    print(f"a // b = {a // b}")

def assignment_operators():
    print("\n=== Assignment Operators ===")
    x = 5
    print(f"x = {x}")
    x += 3
    print(f"x += 3 → {x}")
    x -= 2
    print(f"x -= 2 → {x}")
    x *= 2
    print(f"x *= 2 → {x}")
    x /= 3
    print(f"x /= 3 → {x}")
    x %= 4
    print(f"x %= 4 → {x}")
    x **= 2
    print(f"x **= 2 → {x}")
    x //= 2
    print(f"x //= 2 → {x}")

def comparison_operators():
    print("\n=== Comparison Operators ===")
    a, b = 10, 20
    print(f"a == b → {a == b}")
    print(f"a != b → {a != b}")
    print(f"a > b → {a > b}")
    print(f"a < b → {a < b}")
    print(f"a >= b → {a >= b}")
    print(f"a <= b → {a <= b}")

def logical_operators():
    print("\n=== Logical Operators ===")
    a, b = True, False
    print(f"a and b → {a and b}")
    print(f"a or b → {a or b}")
    print(f"not a → {not a}")

def identity_operators():
    print("\n=== Identity Operators ===")
    a = [1, 2]
    b = a
    c = [1, 2]
    print(f"a is b → {a is b}")
    print(f"a is c → {a is c}")
    print(f"a is not c → {a is not c}")

def membership_operators():
    print("\n=== Membership Operators ===")
    items = [1, 2, 3, 4]
    print(f"2 in items → {2 in items}")
    print(f"5 not in items → {5 not in items}")

def bitwise_operators():
    print("\n=== Bitwise Operators ===")
    a, b = 5, 3  # 101 & 011
    print(f"a & b → {a & b}")
    print(f"a | b → {a | b}")
    print(f"a ^ b → {a ^ b}")
    print(f"~a → {~a}")
    print(f"a << 1 → {a << 1}")
    print(f"a >> 1 → {a >> 1}")

if __name__ == "__main__":
    arithmetic_operators()
    assignment_operators()
    comparison_operators()
    logical_operators()
    identity_operators()
    membership_operators()
    bitwise_operators()