# Say that you are a traveler on a 2D grid. You begin in the top-left corner and
# your goal is to travel to the bottom-right corner.  You may only move down or
# right.  In how many ways can you travel to the goal on a grid with m * n 
# dimensions?


# Time Complexity:  O(2^n)
# Space Complexity: O(n)
def grid_traveler(m, n):

    # base case (0,n) or (m, 0) are grids that have no path 
    if m == 0 or n == 0: return 0
    # base case (1,1) has exactly one path 
    if m == 1 and n == 1: return 1

    # traverse left then right
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


#print(grid_traveler(1, 1))   # 1
#print(grid_traveler(2, 3))   # 3
#print(grid_traveler(3, 2))   # 3
#print(grid_traveler(3, 3))   # 6
#print(grid_traveler(18, 18)) # 2333606220  SLOW!


# 
# Time Complexity:  O(n)
# Space Complexity: O(n)
def grid_traveler_memoization(m, n, mem):

    key = f"{m},{n}"

    # is (m,n) in memo
    if key in mem.keys(): return mem[key]

    # base case (0,n) or (m, 0) are grids that have no path 
    if m == 0 or n == 0: return 0
    # base case (1,1) has exactly one path 
    if m == 1 and n == 1: return 1

    # traverse left then right
    mem[key] = grid_traveler_memoization(m - 1, n, mem) \
        + grid_traveler_memoization(m, n - 1, mem)

    return mem[key]


print(grid_traveler_memoization(1, 1, {}))   # 1
print(grid_traveler_memoization(2, 3, {}))   # 3
print(grid_traveler_memoization(3, 2, {}))   # 3
print(grid_traveler_memoization(3, 3, {}))   # 6
print(grid_traveler_memoization(18, 18, {})) # 2333606220  FAST!
