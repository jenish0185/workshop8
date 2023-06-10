nums = []
while True:
    try:
        num = input("Enter a number (press ! to stop) :")
        if not num :
            break
        num = float(num)
        nums.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if not nums:
    print("No numbers entered")
else:
    avg = sum(nums) / len(nums)
    print("The average of the numbers is ;", avg)
    