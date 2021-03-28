from random import shuffle


# Time complexity O(n log(n)) partition time (n) * recursive function calls (log(n))
# Space complexity O(log(n)) it uses extra space only for storing recursive function calls
def quick_sort(array):
    # Shuffle array to prevent bad partitions (unbalanced partitions).  Unbalanced partitions can
    # result in up to N partition sorts ( n ^ 2 time complexity)
    shuffle(array)
    sort(array, 0, len(array) - 1)

def sort(array, low, high):
    if high <= low: return
    partition_index = partition(array, low, high)
    sort(array, low, partition_index - 1)
    sort(array, partition_index + 1, high)

def partition(array, low, high):
    i, j, partition_item = low, high + 1, array[low]
    while True:
        # scan left, scan right, check for complete scan, swap
        # stop at the left index >= the partition value
        i += 1
        while array[i] < partition_item:
            if i == high: break
            i += 1
        j -= 1
        # stop at the right index <= the partition value
        while partition_item < array[j]:
            if j == low: break
            j -= 1
        # if the left index has crossed the right index, leave the loop
        if i >= j: break
        # swap: (sorting around the partition value)
        # put the left value >= the partition value on the right
        # put the right value <= the partition value on the left
        swap(array, i, j)

    swap(array, low, j)
    # return the 
    return j


def swap(array, x, y):
    tmp = array[x]
    array[x] = array[y]
    array[y] = tmp 

if __name__ == '__main__':
    a = [9, 1, 3, 4, 23, 0]
    quick_sort(a)
    print(a)
