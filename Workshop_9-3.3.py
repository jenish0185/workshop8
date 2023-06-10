while True:
    try:
        money = float(input("Enter an amount of money :"))
        if money < 10000:
            raise ValueError("The amount must be greater that 10,000.")
        break
    except ValueError as e:
        print(e)