
def sort(arr):
    # Selection Sort implementation n^2 complexity
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr1 = [3, 5, 1, 99, 2]
arr2 = [8, 0, 3, 1]
sort(arr1)
sort(arr1)
print(arr1)
print(arr1)
