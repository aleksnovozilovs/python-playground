try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    result = first_number + second_number
    print(f"Result: {result}")
except ValueError:
    print("Please enter numbers only")