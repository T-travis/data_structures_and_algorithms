

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class CustomStack:
    
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, value):
        if self.top:
            temp = self.top
            self.top = Node(value)
            self.top.next = temp
        else:
            self.top = Node(value)
        self.size += 1
            
    def pop(self):
        if self.top is None:
            return None
        
        val = self.top.value
        self.top = self.top.next
        self.size -= 1
        return val
    
    def peek(self):
        return self.top.value
    
    def __str__(self):
        if self.top is None:
            return "None"
        str_representation = "[" + str(self.top.value)
        temp = self.top.next
        while temp:
            str_representation += f", {str(temp.value)}"
            temp = temp.next
        return str_representation + "]"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__str__()})" 
        

if __name__ == '__main__':
    stack = CustomStack()
    print(repr(stack))
    print(stack)
    stack.push(1)
    stack.push(2)
    print(stack)
    assert stack.peek() == 2
    assert stack.pop() == 2
    
