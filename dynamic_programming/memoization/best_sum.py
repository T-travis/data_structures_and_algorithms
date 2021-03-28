# Write a function best_sum(target_sum: int, numbers: [int]) that should return an 
# array containing the shortest combination of numbers that add up to exactly the
# target sum.  If there's a tie, return any of the shortest.

# m = target sum
# n = length of numbers

# Time Complexity:  O(n^m * n)
# Space Complexity: O(m^2)  
def best_sum(target_sum, numbers):
    
    if target_sum == 0: return []

    if target_sum < 0: return None

    shortest_combination = None

    for num in numbers:
        result = best_sum(target_sum - num, numbers)
        if result is not None:
            combination = result + [num]
            if not shortest_combination or len(combination) < len(shortest_combination):
                shortest_combination = combination
             
    return shortest_combination

# print(best_sum(7, [5,3,4,7]))      # [7]
# print(best_sum(8, [2,3,5]))        # [3,5]
# print(best_sum(8, [1,4,5]))        # [4,4]
# print(best_sum(100, [1,2,5,25]))   # [25,25,25,25] SLOW!


# Time Complexity:  O(m * n * m) keys * length of numbers array * keys for building array
# Space Complexity: O(m^2) there are m keys that can have an array each  
def best_sum_momoization(target_sum, numbers, mem):

    if target_sum in mem.keys(): return mem[target_sum]
    
    if target_sum == 0: return []

    if target_sum < 0: return None

    shortest_combination = None

    for num in numbers:
        result = best_sum_momoization(target_sum - num, numbers, mem)
        if result is not None:
            combination = result + [num]
            if not shortest_combination or len(combination) < len(shortest_combination):
                shortest_combination = combination
             
    mem[target_sum] = shortest_combination
    return shortest_combination

print(best_sum_momoization(7, [5,3,4,7], {}))      # [7]
print(best_sum_momoization(8, [2,3,5], {}))        # [3,5]
print(best_sum_momoization(8, [1,4,5], {}))        # [4,4]
print(best_sum_momoization(100, [1,2,5,25], {}))   # [25,25,25,25] FAST!
