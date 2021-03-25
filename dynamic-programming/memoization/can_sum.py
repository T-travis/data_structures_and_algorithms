# Write a function can_sum(target_sum, numbers) that takes a target and
# an array of numbers.  The function should return a boolean indcating  
# whether or not it is possible to generate the target_sum using numbers   
# from the array.

# Time Complexity:  O(n^m)
# Space Complexity: O(n)
def can_sum(target_sum, numbers):
    
    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        
        if can_sum(target_sum - num, numbers):
            return True

    return False

    
# print(can_sum(7, [2, 3]))       # True
# print(can_sum(7, [5, 3, 4, 7])) # True
# print(can_sum(7, [2, 4]))       # False
# print(can_sum(8, [2, 3, 5]))    # True
# print(can_sum(300, [7, 14]))    # False this is SLOW!


# Time Complexity:  O(n)
# Space Complexity: O(n)
def can_sum_memoization(target_sum, numbers, mem):

    if target_sum in mem.keys():
        return mem[target_sum]
    
    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in numbers:
        
        if can_sum_memoization(target_sum - num, numbers, mem):
            mem[target_sum] = True
            return True


    mem[target_sum] = False
    return False

    
print(can_sum_memoization(7, [2, 3], {}))       # True
print(can_sum_memoization(7, [5, 3, 4, 7], {})) # True
print(can_sum_memoization(7, [2, 4], {}))       # False
print(can_sum_memoization(8, [2, 3, 5], {}))    # True
print(can_sum_memoization(300, [7, 14], {}))    # False this is FAST
