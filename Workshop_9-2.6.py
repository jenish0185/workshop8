def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y
try:
    result=divide(10,0)
    print(result)

except ValueError as e:
    print(e)



