"""
A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and
data which are there in singly linked list.

GFG: https://www.geeksforgeeks.org/doubly-linked-list/
"""


class Empty(Exception):
    pass


class DoublyLinkedList:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next_node):
            self._element = element
            self._prev = prev
            self._next = next_node

    def __init__(self):
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        newest = self._Node(e, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head._prev = newest
        self._head = newest
        self._size += 1

    def add_last(self, e):
        newest = self._Node(e, None, None)
        if self.is_empty():
            self._head = newest
            self._tail = newest
        else:
            self._tail._next = newest
            newest._prev = self._tail
        self._tail = newest
        self._size += 1

    def add_any(self, e, pos):
        newest = self._Node(e, None, None)
        thead = self._head
        i = 0
        while i < pos:
            thead = thead._next
            i += 1
        thead._next.prev = newest
        newest._next = thead._next
        thead._next = newest
        newest._prev = thead
        self._size += 1

    def remove_first(self):
        if self.is_empty():
            raise Empty('Doubly LinkList is Empty')
        value = self._head._element
        self.head = self._head._next
        self._head._prev = None
        self._size -= 1
        return value

    def remove_last(self):
        if self.is_empty():
            raise Empty('Doubly LinkList is Empty')
        thead = self.head
        i = 0
        while i < self._size - 2:
            thead = thead.next
            i += 1
        self._tail = thead
        thead = thead.next
        value = thead._element
        self._tail.next = None
        self._size -= 1
        return value

    def remove_any(self, pos):
        if self.is_empty():
            raise Empty('Doubly LinkList is Empty')
        thead = self._head
        i = 0
        while i < pos:
            thead = thead._next
            i += 1

        remove_node = thead._next
        thead._next = remove_node.next
        remove_node.next.prev = thead
        self._size -= 1
        return remove_node._element

    def display(self):
        thead = self._head
        while thead:
            print(thead._element, end='--->')
            thead = thead._next
        print()


if __name__ == '__main__':
    L = DoublyLinkedList()
    L.add_first(10)
    L.add_first(20)
    L.add_first(30)
    L.add_first(40)
    L.display()
    print('Delete: ', L.remove_first())
    L.add_last(70)
    L.display()
    print('Delete: ', L.remove_last())
    L.display()
    L.add_any(80, 2)
    L.display()
    print('Delete: ', L.remove_any(2))
    L.display()
