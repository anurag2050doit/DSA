"""
Stack is a linear data structure which follows a particular order in which the operations are performed.
The order may be LIFO(Last In First Out) or FILO(First In Last Out).
Mainly the following three basic operations are performed in the stack:

Push: Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed.
If the stack is empty, then it is said to be an Underflow condition.
Peek or Top: Returns top element of stack.
isEmpty: Returns true if stack is empty, else false.


GFG: https://www.geeksforgeeks.org/stack-data-structure-introduction-program/
"""


class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]


if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(10)
    stack.push(15)
    stack.push(82)
    stack.push(11)

    print('Stack: ', stack._data)
    print('Length: ', len(stack))
    print('Is-Empty: ', stack.is_empty())
    print('Popped: ', stack.pop())
    print('Top: ', stack.top())
    print('Stack: ', stack._data)
