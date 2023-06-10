while True:
    try:
        file_name = input("Enter a file name: ")
        with open(file_name, 'r') as file:
            contents = file.read()
        break
    except FileNotFoundError:
        print*"File not ound. Please enter a valid file name."
    except Exception as not_read:
        print("Error reading file:", not_read)

print("File contents:", contents)