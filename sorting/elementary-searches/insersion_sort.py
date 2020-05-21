
def sort(arr):
    # Insertion Sort implementation 
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1


arr1 = [3, 5, 1, 99, 2]
arr2 = [8, 0, 3, 1]
arr3 = [1]
sort(arr1)
sort(arr2)
sort(arr3)
print(arr1)
print(arr2)
print(arr3)
