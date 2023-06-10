def concatenate_strings(str1, str2):
    try:
        result = str1 + str2
        return result
    except TypeError:
        print("Error: Both arguments must be strings.")

str1='jenish'
str2=4
if __name__=='__main__':
    concatenate_strings(str1, str2)