class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.front = None
        self.size = 0

    def add(self, value):
        """Push a new node at the end of the list."""

        node = Node(value)

        if self.front is None:
            self.front = node
        else:
            current = self.front
            while current.next:
                current = current.next
            current.next = node

        self.size += 1
    
    def __str__(self):
        """Return string representation of list."""

        res = []
        current = self.front

        while current:
            res.append(current.value)
            current = current.next

        return str(res)

    # Reverse a linked list
    def reverse(self, head):
        # Recursive Solution
        if not head:
            return head
        
        def _reverse(prev, curr, nxt):
            
            if not curr.next:
                curr.next = prev
                return curr
            
            curr.next = prev
            prev = curr
            curr = nxt 
            nxt = curr.next
            
            return _reverse(prev, curr, nxt)
            
        self.front = _reverse(None, head, head.next)

    def reverse_iterative(self, head):
        # Iterative Solution
        if not head:
            return head
        
        prev, curr, nxt = None, head, head.next
        
        while curr.next:

            curr.next = prev
            prev = curr
            curr = nxt
            nxt = curr.next
            
        curr.next = prev
        
        self.front = curr
            


if __name__ == '__main__':
    ll = SinglyLinkedList()
    for i in range(5):
        ll.add(i)
    print(ll)
    ll.reverse(ll.front)
    print(ll)
    ll.reverse_iterative(ll.front)
    print(ll)
    