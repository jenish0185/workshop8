while True:
    try:
        num1 = int(input("enter the first integer :"))
        num2 = int(input("enter the second integer :"))
        result = num1 / num2
        print(f"{num1}/{num2} = {result}")
        break
    except ValueError:
        print("Invalid input. Please enter integers only.")
    except ZeroDivisionError:
        print("Error: division by zero.")