def sum_int(num1, num2):
    try:
        if isinstance(num1, int) and isinstance(num2, int):
            return num1 + num2
        else:
            raise Exception("Given variable(s) are not integers.")
    except Exception as e:
        print("Exception occurred while adding the 2 given variables:", e)


