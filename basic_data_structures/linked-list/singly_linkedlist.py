class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.front = None
        self.last = None
        self.size = 0

    def add(self, value):
        """Push a new node at the end of the list."""

        node = Node(value)
        if self.front is None:
            self.front = node
            self.last = self.front
            self.size += 1
        else:
            self.last.next = node
            self.last = node
            self.size += 1

    def pop(self):
        """Remove a node from the end of the list."""

        if self.front is None:
            raise Exception('Nothing to pop!')
        # only one node
        elif self.front.next is None:
            result = self.front.value
            self.front = None
            self.size -= 1
            return result
        # more than one node, find one before last 
        else:
            current = self.front
            while current.next.next:
                current = current.next
            result = current.next.value
            current.next = None
            self.last = current
            self.size -= 1
            return result

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
            self.size -= 1
        else:
            current = self.front
            while current.next and current.next.value != target:
                current = current.next
            current.next = current.next.next
            self.size -= 1

    def __str__(self):
        """Return string representation of list."""

        llist = []
        current = self.front
        while current:
            llist.append(current.value)
            current = current.next
        return str(llist)
