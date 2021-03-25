# Write a function can_sum(target_sum, numbers) that takes a target and
# an array of numbers.  The function should return a boolean indcating  
# whether or not it is possible to generate the target_sum using numbers   
# from the array.

# m = target, n = length of numbers array
# Time Complexity:  O(m*n)
# Space Complexity: O(m)
def can_sum(target_sum, numbers):

    table = [False for _ in range(target_sum + 1)]
    table[0] = True

    for i in range(len(table)):
        if i > 0 and not table[i]:
            continue
        for num in numbers:
            if (num + i) < len(table):
                table[num+i] = True

    return table[-1]


# Example can_sum(7, [2, 3]) shows each element of the array (7+1 = length) that's T can be summed from an 
# element in the numbers array.  Further, the last element represents if the target value can be summed.
# The indices + numsers[index] show the sum which we are checking if that equals the target.
# indices: 0  1  2  3  4  5  6  7
#         [T, F, T, T, T, T, T, T]
print(can_sum(7, [2, 3]))       # True
print(can_sum(7, [5, 3, 4, 7])) # True
print(can_sum(7, [2, 4]))       # False
print(can_sum(8, [2, 3, 5]))    # True
print(can_sum(300, [7, 14]))    # False
