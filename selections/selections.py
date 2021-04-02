# Finding Kth Smallest/Largest element of an array.
# Method 1: Sorting
#   * Time Complexity is dependent on sort algorithm
#   * smallest using  ascending order & largest using descending order (k is index = k - 1)
# Method 2: Heap Min/Max
#   * Time Complexity with Max Heap O(n + k * log(n)) = n build heap + k times remove * heapify each remove
#   * Time Complexity with Min Heap O(n + (n-k+1) * log(n-k+1))
#   * Max Heap Kth largest = remove/pop the max heap value Kth times where the Kth is the answer
#   * Min Heap Kth largest = remove the max heap value (n - k + 1) where n is the heap size and n - k + 1 is the answer
# https://www.youtube.com/watch?v=aXJ-p3Qa4TY

from random import shuffle


# This is the Quick Select Algorithm finding the Kth smallest element in a given array
# Time Complexity O(n) best case, O(n^2) worst case
# Space Complexity O(1)
def kthsmallest(array, k):
    k -= 1  # account for a zero based array
    shuffle(array)
    low, high = 0, len(array) - 1
    
    while high > low:
        j = partition(array, low, high)
        if k == j: return array[k]
        elif j > k: high = j - 1
        elif j < k: low = j + 1

    return array[k]

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
    a = [9, 1, 3, 4, 23, 0]  # [0, 1, 3, 4, 9, 23]
    for _ in range(10):
        assert kthsmallest(a, 1) == 0
        assert kthsmallest(a, 2) == 1
        assert kthsmallest(a, 3) == 3
        assert kthsmallest(a, 4) == 4
        assert kthsmallest(a, 5) == 9
        assert kthsmallest(a, 6) == 23

