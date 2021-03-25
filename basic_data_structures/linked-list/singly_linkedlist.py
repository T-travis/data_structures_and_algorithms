class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

# Space Complexity is always O(n)
# Time Complexity:
# add: O(1)
# pop: O(1)
# index, contains, delete: O(n)
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

    def pop(self):
        """Remove a node from the end of the list."""
        
        if self.front is None:
            raise Exception('Nothing to pop!')
        
        # if only one element
        if not self.front.next:
            val = self.front.value
            self.front = None
            self.size -= 1
            return val

        current = self.front
        while current.next and current.next.next:
            current = current.next

        val = current.next.value
        current.next = None
        self.size -= 1

        return val

    def index(self, target):
        """Get index of target or return -1."""

        current = self.front
        index = 0

        while current:
            if current.value == target:
                return index
            index += 1
            current = current.next

        return -1

    def contains(self, target):
        """Returns True is target is in the list and false otherwise."""

        return self.index(target) != -1

    def delete(self, target):
        """Delete target from list."""

        if not self.contains(target):
            raise Exception('No such value exists!')
        elif self.front.value == target:
            self.front = self.front.next
        else:
            current = self.front
            while current.next and current.next.value != target:
                current = current.next

            current.next = current.next.next
        
        self.size -= 1

    def __str__(self):
        """Return string representation of list."""

        res = []
        current = self.front

        while current:
            res.append(current.value)
            current = current.next

        return str(res)


if __name__ == "__main__":
    llist = SinglyLinkedList()
    #llist.pop()
    llist.add(1)
    llist.add(2)
    llist.add(3)
    print(f"list: {llist} size: {llist.size}")
    print(llist.index(1))
    print(llist.index(2))
    print(llist.index(3))
    print(llist.contains(1))
    print(llist.contains(2))
    print(llist.contains(3))
    print(llist.contains(4))
    llist.delete(1)
    print(llist)
    print(llist.pop())
    print(f"list: {llist} size: {llist.size}")
    print(llist.pop())
    print(f"list: {llist} size: {llist.size}")
    llist.add(1)
    llist.add(2)
    llist.add(3)
    print(f"list: {llist} size: {llist.size}")
    llist.delete(2)
    print(f"list: {llist} size: {llist.size}")
