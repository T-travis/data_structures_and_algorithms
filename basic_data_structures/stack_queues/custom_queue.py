

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
        
class CustomQueue:
    
    def __init__(self):
        self.front = None
        self.back = None
        
    def enqueue(self, value):
        if self.front:
            temp = self.front
            self.front = Node(value)
            self.front.next = temp
            temp.prev = self.front
        else:
            self.front = Node(value)
            self.back = self.front  
            self.back.prev = self.front
            
            
    def dequeue(self):
        if self.front is None:
            return None
        
        val = self.back.value
        if self.front == self.back:
            self.front, self.back = None, None
        else:
            self.back = self.back.prev
            self.back.next = None
        return val
    
    def peek(self):
        return self.front.value
            
    def __str__(self):
        str_representation = "["
        temp = self.front 
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
    
