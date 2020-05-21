# Multiple Pointers - averagePair
# Write a function called averagePair. Given a sorted array of integers and a target average,
# determine if there is a pair of values in the array where the average of the pair equals the
# target average. There may be more than one pair that matches the average target.

# Bonus Constraints:

# Time: O(N)

# Space: O(1)


def average_pair(array, target_average):
    pointer1 = 0
    pointer2 = 1
    while pointer1 >= 0 and pointer2 < len(array):
        if (array[pointer1] + array[pointer2]) / 2 == target_average:
            return True
        elif (array[pointer1] + array[pointer2]) / 2 < target_average:
            pointer1 += 1
            pointer2 += 1
        else:
            pointer1 -= 1

    return False


assert average_pair([1, 2, 3], 2.5)
assert average_pair([1, 3, 3, 5, 6, 7, 10, 12, 19], 8)
assert average_pair([-1, 0, 3, 4, 5, 6], 4.1) is False
assert average_pair([], 4) is False
