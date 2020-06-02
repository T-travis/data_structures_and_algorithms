from singlylinkedlist import SinglyLinkedList


llist = SinglyLinkedList()
#llist.pop()
llist.add(1)
llist.add(2)
llist.add(3)
print(f"list: {llist} size: {llist.size}")
#llist.pop()
#print(f"list: {llist} size: {llist.size}")
print(llist.index(1))
print(llist.index(2))
print(llist.index(3)) # was poped
print(llist.contains(1))
print(llist.contains(2))
print(llist.contains(3))
llist.delete(1)
print(llist)