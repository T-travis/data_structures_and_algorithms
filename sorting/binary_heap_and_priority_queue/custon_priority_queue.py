
# Priority Queue = data structure that keeps data stored by it's weight/importance.
# Binary Heap will allow us both enqueue and dequeue items in O(log n)
# which is great for implementing a Priority Queue.
# We will want to insert according to priority and remove according to priority.
# 
class PriorityQueue:

    def __init__(self):
        # index 0 is not used to allow integer division, so index 1 is the start
        self.heap_list = [{'key': None, 'value': None}]  
        self.size = 0

    def insert(self, key, value):
        # append element at the end of the list, increment list size,
        # and percolate the element up to its correct position
        self.heap_list.append({'key': key, 'value': value})
        self.size += 1
        self.percolate_up(self.size)

    def percolate_up(self, i):
        while i // 2 > 0:
            # if less than parent, swap values
            if self.heap_list[i]['key'] > self.heap_list[i // 2]['key']:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            # move up to parent position
            i //= 2

    def delete_max(self):
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
            if self.heap_list[i]['key'] < self.heap_list[min_child_index]['key']:
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
            if self.heap_list[i * 2]['key'] > self.heap_list[i * 2 + 1]['key']:
                return i * 2
            else:
                # return right child index
                return i * 2 + 1


if __name__ == '__main__':

    pq = PriorityQueue()
    objects = [{'key':5, 'value':'five'}, {'key':9, 'value':'nine'}, {'key':11, 'value':'eleven'}, \
            {'key': 14, 'value': 'fourteen'}, {'key': 18, 'value': 'eighteen'}, {'key': 19, 'value': 'nineteen'}, \
            {'key': 21, 'value': 'twenty'}, {'key': 33, 'value': 'thrity three'}, {'key': 17, 'value': 'seventeen'}, \
            {'key':27, 'value':'twenty seven'}]

    for obj in objects:
        pq.insert(obj['key'], obj['value'])

    i = 0
    keys = []
    for obj in pq.heap_list:
        if i > 0:
            keys.append(obj['key'])
        i += 1

    # check keys/weights are in same order
    # visual check https://visualgo.net/en/heap
    assert keys == [33,27,19,17,21,9,18,5,14,11]

    max_obj = pq.delete_max()
    print(max_obj)

    i = 0
    keys = []
    for obj in pq.heap_list:
        if i > 0:
            keys.append(obj['key'])
        i += 1

    assert keys == [27,21,19,17,11,9,18,5,14]