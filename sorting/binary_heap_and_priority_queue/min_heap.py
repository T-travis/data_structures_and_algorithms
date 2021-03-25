
# BINARY HEAP will allow us both enqueue and dequeue items in O(log n)

# LEFT CHILD of a parent (at position p) is the node that is found in position 2p in the list
# RIGHT CHILD of the parent is at position 2p+1 in the list
# PARENT is at position n/2, given that a node is at position n in the list

# Example:
# indices -> 0, 1,  2,  3,  4,  5,  6,  7,  8,  9        
# values  -> 5, 9, 11, 14, 18, 19, 21, 33, 17, 27


class MinBinaryHeap:

    def __init__(self):
        # index 0 is not used to allow integer division, so index 1 is the start
        self.heap_list = [0]  
        self.size = 0

    def insert(self, element):
        # append element at the end of the list, increment list size,
        # and percolate the element up to its correct position
        self.heap_list.append(element)
        self.size += 1
        self.percolate_up(self.size)

    def percolate_up(self, i):
        while i // 2 > 0:
            # if less than parent, swap values
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            # move up to parent position
            i //= 2

    def delete_min(self):
        # set the last to be first deleting the first
        # delete last and decrement the size
        # percolutate the root element down to its proper place
        min_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.heap_list.pop()
        self.size -= 1
        self.percolate_down(1)  # index 1 is the start
        return min_val

    def percolate_down(self, i):
        while (i * 2) <= self.size:
            min_child_index = self.min_child(i)
            # if parent is greater than the min child, percolate down
            if self.heap_list[i] > self.heap_list[min_child_index]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child_index]
                self.heap_list[min_child_index] = tmp
            i = min_child_index

    def min_child(self, i):
        # if the right child index > size of heap_list, return left child index
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            # if left child < right child, return left child index
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                # return right child index
                return i * 2 + 1


if __name__ == '__main__':

    min_heap = MinBinaryHeap()
    values = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

    for value in values:
        min_heap.insert(value)

    # skip 0 index not used in heap
    assert min_heap.heap_list[1:] == values