def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("-----------------")
    print("Operations: +  -  *  /")

    while True:
        expr = input("\nEnter expression (e.g. 3 + 4) or 'q' to quit: ").strip()
        if expr.lower() == "q":
            break

        parts = expr.split()
        if len(parts) != 3:
            print("Invalid format. Use: number operator number")
            continue

        try:
            a, op, b = float(parts[0]), parts[1], float(parts[2])
        except ValueError:
            print("Invalid numbers.")
            continue

        try:
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = subtract(a, b)
            elif op == "*":
                result = multiply(a, b)
            elif op == "/":
                result = divide(a, b)
            else:
                print(f"Unknown operator: {op}")
                continue
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
