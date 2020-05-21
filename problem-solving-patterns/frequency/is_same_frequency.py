# Write a function called sameFrequency. Given two positive integers,
# find out if the two numbers have the same frequency of digits.

# Your solution MUST have the following complexities:

# Time: O(N)


def is_same_frequency(int1, int2):
    # check if null, not int type, or negative number
    if int1 is None or int2 is None or not isinstance(int1, int) or not isinstance(int2, int):
        raise TypeError
    if int1 < 0 or int2 < 0:
        raise ValueError

    int1_frequency = make_frequency(int1)
    int2_frequency = make_frequency(int2)
    if len(int1_frequency) <= 0 or len(int1_frequency) != len(int2_frequency):
        return False
    for key in int1_frequency:
        if key not in int2_frequency or int1_frequency[key] != int2_frequency[key]:
            return False

    return True


def make_frequency(num):
    frequency = {}
    if num < 0:
        num = -1 * num
    while num // 10 != 0:
        right_digit = num % 10
        if right_digit in frequency:
            frequency[right_digit] = frequency[right_digit] + 1
        else:
            frequency[right_digit] = 1
        num = num // 10
    right_digit = num % 10
    if right_digit in frequency:
        frequency[right_digit] = frequency[right_digit] + 1
    else:
        frequency[right_digit] = 1
    return frequency


assert is_same_frequency(2344, 5) is False
assert is_same_frequency(232, 52) is False
assert is_same_frequency(2, 2) is True
assert is_same_frequency(123, 231) is True


