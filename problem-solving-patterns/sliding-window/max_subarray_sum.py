# Sliding Window - maxSubarraySum
# Given an array of integers and a number, write a function called maxSubarraySum,
# which finds the maximum sum of a subarray with the length of the number passed to the function.

# Note that a subarray must consist of consecutive elements from the original array.
# In the first example below, [100, 200, 300] is a subarray of length 3 of [100,200,300,400],
# but [100, 300] is not.


def max_subarray_sum(array, sub_len):
    # return None for an empty array or when the sub length value
    # is greater than the length of the array
    if len(array) == 0 or sub_len > len(array):
        return None
    start_index, max_sum = 0, 0
    while start_index + (sub_len - 1) < len(array):
        new_max = 0
        for i in range(sub_len):
            new_max += array[start_index + i]
        if new_max > max_sum:
            max_sum = new_max
        start_index += 1
    return max_sum


assert max_subarray_sum([100, 200, 300, 400], 2) == 700
assert max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39
assert max_subarray_sum([-3, 4, 0, -2, 6, -1], 2)
assert max_subarray_sum([3, -2, 7, -4, 1, -1, 4, -2, 1], 2) == 5
assert max_subarray_sum([], 1) is None
assert max_subarray_sum([2, 3], 3) is None
