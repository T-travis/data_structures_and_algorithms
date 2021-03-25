from collections import deque  # uses a doubly linked list under the hood
# deque class supports O(1) for adding and removing from either
# end so it is good for stacks and queues

# Stacks can be created using a custom linked list but also
# by just using a build in Python List or even better Deque.
# LIFO (last in first out) like stacking paper and removing the last added 

# Space Complexity O(n)
# Time Comlexity O(1)
class Stack:

    def __init__(self):
        self.list = deque()
        
    def push(self, value):
        self.list.append(value)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop() 

    def size(self):
        return len(self.list) 

    def peek(self):
        if len(self.list) == 0:
            return None
        return self.list[-1]

    def __str__(self):
        return str(self.list)


stack = Stack()
stack.pop()
print(stack)
stack.push('first')
print('size: ' + str(stack.size()))
print(stack)
stack.push('second')
print('size: ' + str(stack.size()))
print(stack)
stack.push('3rd')
print('size: ' + str(stack.size()))
print(stack)
print(stack.pop())
print('size: ' + str(stack.size()))
print(stack)
print(stack.peek())
print(stack.pop())
print('size: ' + str(stack.size()))
print(stack)
