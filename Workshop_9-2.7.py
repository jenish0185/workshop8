my_list = [1,2,3,4,5]

try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range")
    