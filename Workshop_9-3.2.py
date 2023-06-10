while True:
    try:
        numerator = float(input("Enter the numerator :"))
        denominator = float(input("Enter the dominator :"))
        result=numerator/denominator
        print(f"The result is {result}")
        break
    except ValueError:
        print("Error. Please enter a numeric value")
    except ZeroDivisionError:
        print("Can't divide by zero. Please enter a non-zero value for denominator")