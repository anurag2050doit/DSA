"""
Operations on Deque:
Mainly the following four basic operations are performed on queue:

insertFront(): Adds an item at the front of Deque.
insertLast(): Adds an item at the rear of Deque.
deleteFront(): Deletes an item from front of Deque.
deleteLast(): Deletes an item from rear of Deque.

In addition to above operations, following operations are also supported
getFront(): Gets the front item from queue.
getRear(): Gets the last item from queue.
isEmpty(): Checks whether Deque is empty or not.

GFG: https://www.geeksforgeeks.org/deque-set-1-introduction-applications/
"""


class Empty(Exception):
    pass


class ArrayDeque:

    def __init__(self):
        self._data = []
        self._front = 0

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty('Deque is Empty')

        return self._data[self._front]

    def add_first(self, e):
        self._data.insert(self._front, e)

    def add_last(self, e):
        self._data.append(e)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        value = self._data.pop(self._front)
        return value

    def delete_last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        value = self._data.pop()
        return value


if __name__ == '__main__':
    d = ArrayDeque()
    d.add_first(10)
    d.add_last(20)
    d.add_last(30)
    d.add_last(40)
    print('Deques: ', d._data)
    print('Delete Last', d.delete_last())
    print('Delete first', d.delete_first())
