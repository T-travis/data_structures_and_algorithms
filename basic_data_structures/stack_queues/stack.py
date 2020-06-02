from collections import deque  # uses a doubly linked list under the hood
# deque class supports O(1) for adding and removing from either
# end so it is good for stacks and queues

# Stacks can be created using a custom linked list but also
# by just using a build in Python List or even better Deque.
# LIFO (last in first out) like stacking paper and removing the last added 


class Stack:

    def __init__(self):
        self.list = deque()
        
    def push(self, value):
        if self._valid_input(value):
            raise Exception('Arguments can not be None type!')
        self.list.append(value)

    def pop(self):
        if self.size() == 0:
            raise Exception('The stack is empty already!')
        self.list.pop() 

    def size(self):
        return len(self.list) 

    def peek(self):
        if self.size() == 0:
            raise Exception('The stack is empty!')
        return self.list[-1]

    def __str__(self):
        return str(self.list)

    def _valid_input(self, value):
        return value == None


stack = Stack()
#stack.pop()
#stack.push(None)
print(stack)
stack.push('first')
print(stack.size())
print(stack)
stack.push('second')
print(stack.size())
print(stack)
stack.push('3rd')
print(stack.size())
print(stack)
stack.pop()
print(stack.size())
print(stack)
print(stack.peek())
