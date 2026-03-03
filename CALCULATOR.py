def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if choice == '1':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                try:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                except ZeroDivisionError:
                    print("Error! Division by zero.")
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
calculator()

