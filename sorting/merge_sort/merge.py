# Merge two sorted arrays into a new sorted array
def merge(arr1, arr2):
    arr1_index, arr2_index = 0, 0
    aux_array = []
    while arr1_index < len(arr1) and arr2_index < len(arr2):
        if arr1[arr1_index] < arr2[arr2_index]:
            aux_array.append(arr1[arr1_index])
            arr1_index += 1
        else:
            aux_array.append(arr2[arr2_index])
            arr2_index += 1
    while arr1_index < len(arr1):
        aux_array.append(arr1[arr1_index])
        arr1_index += 1
    while arr2_index < len(arr2):
        aux_array.append(arr2[arr2_index])
        arr2_index += 1
    return aux_array


arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 4]
print(merge(arr1, arr2))
