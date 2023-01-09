#!/usr/bin/python3
def roman_to_int(roman_string):
    """
     a function that converts a Roman numeral to an integer.
     """
    # Largest to smallest, add them up
    # smaller before larger , subtract smaller
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
             "D": 500, "M": 1000}
    result = 0
    if type(roman_string) is str:
        for i in range(len(roman_string)):
            if i+1 < len(roman_string) and (roman[roman_string[i]]
                                            < roman[roman_string[i+1]]):
                result -= roman[roman_string[i]]
            else:
                result += roman[roman_string[i]]
        return result
    else:
        return 0
