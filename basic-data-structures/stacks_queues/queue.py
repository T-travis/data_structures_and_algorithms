from collections import deque  # uses a doubly linked list under the hood
# deque class supports O(1) for adding and removing from either
# end so it is good for stacks and queues

# Queues can be created using a custom linked list or build in list (to SLOW) or 
# even better using Dequeue.  They support FIFO (first in first out)
# operations in O(1)


class Queue:

    def __init__(self):
        self.list = deque()

    def enqueue(self, value):
        if self._valid_input(value):
            raise Exception('None is an invalid arguement!')
        self.list.append(value)

    def dequeue(self):
        if self.size() == 0:
            raise Exception('The queue is empty!')
        value = self.list.popleft()
        return value

    def size(self):
        return len(self.list)

    def peek(self):
        if self.size() == 0:
            raise Exception('The queue is empty!')
        return self.list[0]

    def _valid_input(self, value):
        return value == None

    def __str__(self):
        return str(self.list)


q = Queue()
#print(q.peek())
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
print('size: ' + str(q.size()))
print(q.dequeue())
print(q)
print(q.peek())
