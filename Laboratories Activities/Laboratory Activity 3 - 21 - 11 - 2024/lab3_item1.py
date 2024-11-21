def roman_numerals(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    roman = roman.upper()
    total = 0
    prev_value = 0

    for char in reversed(roman):
        value = roman_values[char]
        if value < prev_value:
            total -= value  
        else:
            total += value 
        prev_value = value

    return total


if __name__ == "__main__":
    roman = input("Enter a Roman numeral: ")
    try:
        result = roman_numerals(roman)
        print(f"The integer value of '{roman.upper()}' is: {result}")
    except KeyError:
        print("Invalid Roman numeral entered!")