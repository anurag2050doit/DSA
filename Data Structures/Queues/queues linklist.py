"""
In a Queue data structure, we maintain two pointers, front and rear. The front points the first item of queue and rear
points to last item.

enQueue() This operation adds a new node after rear and moves rear to the next node.

deQueue() This operation removes the front node and moves front to the next node.

GFG: https://www.geeksforgeeks.org/queue-set-2-linked-list-implementation/
"""


class Empty(Exception):
    pass


class LinkedQueue:
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

    def enqueue(self, e):
        new_node = self._Node(e, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return value

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end='-->')
            temp = temp._next
        print()


if __name__ == '__main__':
    q = LinkedQueue()
    q.enqueue(10)
    q.enqueue(20)
    q.display()
    print('Length: ', len(q))
    print('Dequeue: ', q.dequeue())
    q.enqueue(30)
    q.enqueue(40)
    q.display()
    print('Dequeue: ', q.dequeue())
