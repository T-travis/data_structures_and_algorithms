# Frequency Counter / Multiple Pointers - areThereDuplicates
# Implement a function called, areThereDuplicates which accepts
# a variable number of arguments, and checks whether there are any
# duplicates among the arguments passed in.  You can solve this using the
# frequency counter pattern OR the multiple pointers pattern.


def are_there_duplicates(*args):
    frequency = {}
    for arg in args:
        if arg in frequency:
            return True
        else:
            frequency[arg] = 1

    return False


assert are_there_duplicates(1, 2, 3) is False
assert are_there_duplicates(1, 2, 2) is True
assert are_there_duplicates(1, 1, 3) is True
assert are_there_duplicates(1, 2, 3, 4) is False
assert are_there_duplicates(1, 2, 4, 4) is True
