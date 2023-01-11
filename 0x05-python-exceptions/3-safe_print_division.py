#!/usr/bin/python3
def safe_print_division(a, b):
    """
    a function that divides 2 integers and prints the result.
    """
    result = 0
    try:
        result = a / b
        return result
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(result))
