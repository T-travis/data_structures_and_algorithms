# Say that you are a traveler on a 2D grid. You begin in the top-left corner and
# your goal is to travel to the bottom-right corner.  You may only move down or
# right.  In how many ways can you travel to the goal on a grid with m * n 
# dimensions?


# Time Complexity:  O(m * n)
# Space Complexity: O(m * n)
def grid_traveler(m, n):

    table = [[0]*(n+1) for _ in range(m+1)]
    table[1][1] = 1

    for row in range(m+1):
        for column in range(n+1):
            curr = table[row][column]
            pass
            if column+1 <= n:
                table[row][column+1] += curr
            if row+1 <= m:
                table[row+1][column] += curr
 
    return table[m][n]

print(grid_traveler(1, 1))   # 1
print(grid_traveler(2, 3))   # 3
print(grid_traveler(3, 2))   # 3
print(grid_traveler(3, 3))   # 6
print(grid_traveler(18, 18)) # 2333606220
