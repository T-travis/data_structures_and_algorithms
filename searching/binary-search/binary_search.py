# Binary Search Algorithm
# divide and conquer algorithm
# Time Complexity O(log N)
# Space Complexity O(1)

# Algorithm:
# set start and end index for array
# search while the start is <= end
#   get middle index 
#   is middle == target, return middle index
#   is middle > target, end becomes middle index - 1
#   is middle < target, start becomes middle index + 1
# if target is never found return -1


def index_of(arr, target):
    return binary_search(arr, target)


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def index_of_recursive(arr, target):
    return binary_search(arr, target)


def binary_search_recursive(arr, target):

    if len(arr) > 0:

        middle_index = len(arr) // 2

        if arr(middle_index) == target:
            return middle_index

        binary_search_recursive(arr[:middle_index], target)
        binary_search_recursive(arr[middle_index + 1:], target)

    return -1


array = [1, 3, 4, 6, 19, 80]
print(index_of(array, 5))
print(index_of(array, 19))
print(index_of(array, 1))
print(index_of(array, 80))
print()
print(index_of_recursive(array, 5))
print(index_of_recursive(array, 19))
print(index_of_recursive(array, 1))
print(index_of_recursive(array, 80))

