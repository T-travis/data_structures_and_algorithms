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

