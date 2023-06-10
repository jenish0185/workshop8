while True:
    try:
        str_input = input("Enter a string to convert to an integer :")
        int_output = int(str_input)
        print(f"The integer value of '{str_input}' is {int_output}")
        break
    except ValueError:
        print(f"please enter string to convert.'{str_input}' cannot be converted to an integer. Please try again." )