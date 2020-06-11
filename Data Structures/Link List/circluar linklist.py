"""
Circular linked list is a linked list where all nodes are connected to form a circle.
There is no NULL at the end. A circular linked list can be a singly circular linked list or doubly circular
linked list.

GFG: https://www.geeksforgeeks.org/circular-linked-list/
"""


class Empty(Exception):
    pass


class CircularLinkList:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
            newest._next = newest
        else:
            self._tail._next = newest
            newest._next = self._head
        self._head = newest
        self._size += 1

    def add_last(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def add_any(self, e, pos):
        newest = self._Node(e, None)
        thead = self._head
        i = 1
        while i < pos:
            thead = thead._next
            i += 1
        newest._next = thead._next
        thead._next = newest
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('Linked List Empty')
        oldhead = self._tail.next
        self._tail.next = oldhead.next
        self._head = oldhead.next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return oldhead._element

    def remove_last(self):
        if self.is_empty():
            raise Empty('Linked List Empty')
        thead = self._head
        i = 0
        while i < self._size - 2:
            thead = thead.next
            i += 1

        remove = thead.next
        self._tail = thead
        self._tail.next = self._head
        value = remove._element
        self._size -= 1
        return value

    def remove_any(self, pos):
        if self.is_empty():
            raise Empty('Linked List Empty')
        thead = self._head
        i = 0
        while i < pos:
            thead = thead.next
            i += 1

        remove = thead.next
        thead.next = remove.next
        self._size -= 1

    def display(self):
        thead = self._head
        i = 0
        while i < self._size:
            i += 1
            print(thead._element, end='-->')
            thead = thead.next
        print()


if __name__ == '__main__':
    CL = CircularLinkList()
    CL.add_first(78)
    CL.add_first(10)
    CL.add_first(30)
    CL.add_last(80)
    CL.display()
    print('Deleted: ', CL.remove_first())
    CL.display()
    CL.add_first(5)
    CL.display()
    print('Deleted: ', CL.remove_last())
    CL.display()
