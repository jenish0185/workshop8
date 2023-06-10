def large(int_list):
    try:
        if len(int_list) == 0:
            raise ValueError("input list must not be empty.")
        largest = max(int_list)
        return largest
    except ValueError as e:
        print(f"Error: {e}")
large([])