try:
        num1 = int(input("enter the first integer :"))
        num2 = int(input("enter the second integer :"))
        result = num1 / num2
except ZeroDivisionError:
        print("Error: division by zero.")
else:
        print("The result of dividing {} by {}". format(num1, num2, result))