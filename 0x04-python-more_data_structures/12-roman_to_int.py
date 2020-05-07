#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        value = 0
        roman_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        roman_string = list(roman_string)
        result = [roman_int.get(item, item) for item in roman_string]
        for i in range(0, len(result) - 1):
            if result[i] < result[i+1]:
                value -= result[i]
            else:
                value += result[i]
        value += result[-1]
        return value
    else:
        return 0
