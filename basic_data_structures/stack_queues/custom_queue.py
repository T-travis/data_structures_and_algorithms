

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
        
class CustomQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = self.tail.next
            
    def dequeue(self):
        if self.head is None:
            return None
        
        val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
            
        return val
    
    def peek(self):
        return self.head.value
            
    def __str__(self):
        str_representation = "["
        temp = self.head
        if temp:
            str_representation += f"{temp.value}"
            temp = temp.next
        while temp:
            str_representation += f", {temp.value}"
            temp = temp.next 
        return str_representation + "]"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({str(self)})"


if __name__ == '__main__':
    queue = CustomQueue()
    print(queue)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print(repr(queue))
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue)
    print(repr(queue))
    
