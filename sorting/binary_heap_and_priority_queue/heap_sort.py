# Heap Sort
# Algorithm:
# 1. Insert all array values into a min priority queue
# 2. Remove the minimum value from the priority queue and
# 3. Push the minimum value back in array
# 4. Repeat until the priority queue is empty

# import Min Priority Queue
from priority_queue import PriorityQueue


def heap_sort(array):
    min_pq = PriorityQueue()
    for el in array:
        min_pq.push(el, el)  # here the int array is the value and priority/weight

    index = 0  # used to insert back in the array

    while min_pq.size() > 0:
        min_val = min_pq.pop()
        array[index] = min_val[0]
        index += 1

    return array


if __name__ == '__main__':
    array = [9, 3, 4, 1, 23, 0]
    print(heap_sort(array))
