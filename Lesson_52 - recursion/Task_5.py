def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError('input string must be digit string')
    if len(digit_string) <= 1:
        return int(digit_string)
    else:
        first_digit = int(digit_string[0])
        return first_digit + sum_of_digits(digit_string[1:])


print(sum_of_digits('26121'))
print(sum_of_digits('qwe'))