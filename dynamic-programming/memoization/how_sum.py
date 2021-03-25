# Write a function how_sum(target_sum, numbers) that takes in a target sum and an array of
# numbers.  Return an array containing a combination of elements that add up to exactly the target_sum.
# If none exists, return null/None.  If multiple combinations exist, return any single one.


# Time Complexity:  O(n^m*m)
# Space Complexity: O(n)
def how_sum(target_sum, numbers):
    
    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in numbers:
        result = how_sum(target_sum - num, numbers)
        if result is not None:
            return [num] + result



# print(how_sum(7, [2, 3]))       # 
# print(how_sum(7, [5, 3, 4, 7])) #
# print(how_sum(7, [2, 4]))       # None
# print(how_sum(8, [2, 3, 5]))    #
# print(how_sum(300, [7, 14]))    # None, this is SLOW!


# Time Complexity:  O(n*m^2)
# Space Complexity: O(m*2)
def how_sum_memoization(target_sum, numbers, mem):
    
    if target_sum in mem.keys():
        return mem[target_sum]

    if target_sum == 0:
        return []

    if target_sum < 0:
        return None

    for num in numbers:
        result = how_sum_memoization(target_sum - num, numbers, mem)
        if result is not None:
            mem[target_sum] = [num] + result
            return mem[target_sum]

    mem[target_sum] = None
    return None


print(how_sum_memoization(7, [2, 3], {}))       # 
print(how_sum_memoization(7, [5, 3, 4, 7], {})) #
print(how_sum_memoization(7, [2, 4], {}))       # None
print(how_sum_memoization(8, [2, 3, 5], {}))    #
print(how_sum_memoization(300, [7, 14], {}))    # None, this is FAST!
