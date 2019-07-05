"""
A Queue is a linear structure which follows a particular order in which the operations are performed.
The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the
consumer that came first is served first. The difference between stacks and queues is in removing. In a stack we remove
the item the most recently added; in a queue, we remove the item the least recently added.

GFG: https://www.geeksforgeeks.org/queue-data-structure/
"""


class Empty(Exception):
    pass


class ArrayQueue:
    def __init__(self):
        self._data = []
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        self._data.append(e)
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        self._size -= 1
        return value

    def first(self):
        if self.is_empty():
            raise Empty('Queue is Empty')
        return self._data[self._front]

    def __iter__(self):
        return iter(self._data)


if __name__ == '__main__':
    q = ArrayQueue()
    q.enqueue(10)
    q.enqueue(20)
    print('Queue: ', q._data)
    q.dequeue()
    print('Queue: ', q._data)
    q.enqueue(30)
    q.dequeue()
    print('Queue: ', q._data)
    q.enqueue(40)
    print('Queue: ', q._data)
