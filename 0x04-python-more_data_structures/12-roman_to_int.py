#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Dictionary mapping Roman numerals to integers
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    for i in range(len(roman_string) - 1):  # Notice the change here
        # If current numeral is smaller than the next, subtract its value
        if roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            total -= roman_dict[roman_string[i]]
        # Otherwise, add its value
        else:
            total += roman_dict[roman_string[i]]

    # Add the value of the last numeral outside the loop
    total += roman_dict[roman_string[-1]]

    return total
