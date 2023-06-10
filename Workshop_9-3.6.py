def dictionary_value(my_dict, key):
    try:
        value = my_dict[key]
        return value
    except KeyError:
        print(f"Error: The key '{key}' does not exist.")
my_dict = {'id':2004, 'collegeid':4002}
dict_value = dictionary_value(my_dict, 'uni_id')