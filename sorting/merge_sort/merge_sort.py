"""
Merge Sort implementation O(n log n) time complexity, O(n) space complexity.
   Why logn:
    array = [1,2,3,4,5,6,7,8] has three splits, 2^3 = 8 and log8 = 3 (log base 2 or 2^n)
           [1,2,3,4] [5,6,7,8]
         [1,2] [3,4] [5,6] [7,8]
      [1] [2] [3] [4] [5] [6] [7] [8]
    array of length 32 has 5 splits, 2^5 = 32, log32 = 5 (log base 2)
   Why N in O(N logn):
    the merge() has a O(n) time complexity
   Why n space complexity:
    we have to sort an array of size n and so we need to create auxilary arrays
    for n elements of the array to be sorted and thus we have O(n) space complexity
"""


def merge_sort(arr1):
    if len(arr1) <= 1:
        return arr1

    mid = len(arr1) // 2
    left = merge_sort(arr1[0:mid])
    right = merge_sort(arr1[mid:])

    return _merge(left, right)


def _merge(arr1, arr2):

    new_arr = []
    arr1_i = 0
    arr2_i = 0

    while arr1_i < len(arr1) and arr2_i < len(arr2):
        if arr1[arr1_i] < arr2[arr2_i]:
            new_arr.append(arr1[arr1_i])
            arr1_i += 1
        else:
            new_arr.append(arr2[arr2_i])
            arr2_i += 1

    while arr1_i < len(arr1):
        new_arr.append(arr1[arr1_i])
        arr1_i += 1

    while arr2_i < len(arr2):
        new_arr.append(arr2[arr2_i])
        arr2_i += 1

    return new_arr


arr = [99, 1, 202, 3, 0]
print(merge_sort(arr))
