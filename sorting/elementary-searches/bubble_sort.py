
def sort(arr):
    # Bubble Sort implementation n^2 complexity
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j+1] < arr[j]:
                swap(arr, j+1, j)


def swap(arr, less, greater):
    # this works right to left
    arr[less], arr[greater] = arr[greater], arr[less]


arr1 = [3, 5, 1, 99, 2]
arr2 = [8, 0, 3, 1]
arr3 = [2, 1]
sort(arr1)
sort(arr2)
sort(arr3)
print(arr1)
print(arr2)
print(arr3)
