# DYNAMIC ARRAY IMPLEMENTATION

from ctypes import py_object

# Complexity
# space is always O(n)
# time: 
# access    O(1)
# append    O(1)
# pop       O(1)
# insert    O(n)
# remove_at O(n)
class ArrayList:

    def __init__(self):
        self._count = 0  # element count
        self._capacity = 1  # default capacity
        self._array = self._make_array(self._capacity)

    def append(self, element):
        if self._count == self._capacity:
            self._resize(2 * self._capacity)
        
        self._array[self._count] = element
        self._count += 1

    def pop(self):
        if self._count <= 0:
            raise IndexError

        val = self._array[self._count-1]
        self._count -= 1

        return val

    def remove_at(self, index):
        if self._count == 0 or index > self._count or index < 0:
            raise IndexError
        elif self._count-1 == index:
            self._array[index] = 0
            self._count -= 1
        else:
            i = 0
            for i in range(index+1, self._count):
                self._array[i-1] = self._array[i]

            self._array[i] = 0
            self._count -= 1

    def insert(self, element, index):
        if index > self._count or index < 0:
            raise IndexError

        if self._count == self._capacity:
            self._resize(2 * self._capacity)

        # move everything one index forward frpm index
        for i in range(self._count - 1, index - 1, -1):
            self._array[i + 1] = self._array[i]
            
        self._array[index] = element
        self._count += 1

    def __getitem__(self, index):
        if index < 0 or index > self._count:
            raise IndexError
        
        return self._array[index]
    
    def _resize(self, new_capacity):
        temp_new_array = self._make_array(new_capacity)

        for index in range(self._count):
            temp_new_array[index] = self._array[index]
        
        self._array = temp_new_array
        self._capacity = new_capacity
        
    def _make_array(self, new_capacity):
        return (new_capacity * py_object)()

    def __str__(self):
        if self._count <= 0:
            raise IndexError

        res = f"[{self._array[0]}"
        index = 0
        for index in range(1, self._count):
            res += f", {self._array[index]}"
        
        return f"{res}]"


# https://www.geeksforgeeks.org/implementation-of-dynamic-array-in-python/
# https://docs.python.org/3/library/ctypes.html
# ctypes is a foreign function library for Python. It provides C compatible 
# data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.
#
# class ctypes.py_object
#   Represents the C PyObject * datatype. Calling this without an 
#   argument creates a NULL PyObject * pointer.


if __name__ == '__main__':
    array_list = ArrayList()
    array_list.append(11)
    print(array_list)
    array_list.append(22)
    print(array_list)
    print(array_list[0])
    print(array_list[1])
    array_list.insert(123, 0)
    print(array_list)
    array_list.insert(2222, 2)
    print(array_list)
    array_list.remove_at(3)
    print(array_list)
    print(array_list.pop())
    print(array_list)
    print(array_list.pop())
    print(array_list)

