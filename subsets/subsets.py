# https://www.mathsisfun.com/sets/power-set.html
# https://www.mathsisfun.com/activity/subsets.html
# https://www.mathsisfun.com/combinatorics/combinations-permutations.html
# https://www.youtube.com/watch?v=NA2Oj9xqaZQ

# Time Complexity: O(2^n) combinations are possible
# Space Complexity: O(n^2) the most space is the list * itself (arr * arr)

def subsets(arr):
    # see exmpale.png for tree
    # go left = exclude element (don't use first_el)
    # go right = include element (use first_el)
    if not arr: return [[]]

    first_el = arr[0]
    rest_of = arr[1:]
    combinations_without_first = subsets(rest_of)

    combinations_with_first = []

    for combination in combinations_without_first:
        combinations_with_first.append([first_el] + combination)

    # create new list from combinations including the first_el and excluding it
    return combinations_without_first + combinations_with_first


if __name__ == '__main__':
    print(subsets(['a','b','c']))
