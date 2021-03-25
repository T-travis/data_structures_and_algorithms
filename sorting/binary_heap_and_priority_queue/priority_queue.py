import heapq

# A Priority Queue adds and removes according to some priority among the items in the
# queue. { (1, item), (2, item), (5, item), (99, item), ...} where priority is highest
# bases on lowest num in (num, item).  This is built using a Min Heap and in Python
# the "heapq" does just that for you.

# to max it a max heap, assuming integers are used for the ordering, convert the num to -num


class PriorityQueue:

    def __init__(self):
        self.q = []
        self.hq = heapq
        self.count = 0

    def push(self, priority, value):
        self.hq.heappush(self.q, (priority, value))
        self.count += 1

    def pop(self):
        if self.size() == 0:
            raise Exception('PriorityQueue is empty!')
        value = self.hq.heappop(self.q)
        self.count -= 1
        return value 

    def size(self):
        return self.count

    def __str__(self):
        return str(self.q)


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.push(99, 'just programming for fun')
    pq.push(1, 'the world is ending')
    pq.push(4, 'playing video games')
    print(pq)
    print(pq.size())
    print(pq.pop())
    print(pq)
    print(pq.size())
