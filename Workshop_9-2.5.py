numbers = input("Ente integers :")

try:

    number_list = [int(n) for n in numbers.split()] 
    
    total = sum(number_list)
    print("The sum of the numbers is :", total)
except ValueError:
    print("Please enter only integers")