"""
Implement a stack using single linked list concept. all the single linked list operations perform based on Stack
operations LIFO(last in first out) and with the help of that knowledge we are going to implement a stack using
single linked list. using single linked lists so how to implement here it is linked list means what we are storing the
information in the form of nodes and we need to follow the stack rules and we need to implement using single linked list
nodes so what are the rules we need to follow in the implementation of a stack a simple rule that is last in first out
and all the operations we should perform so with the help of a top variable only with the help of top variables are how
to insert the elements let’s see

GFG: https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/
"""


class Empty(Exception):
    pass


class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        return value

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._head._element

    def display(self):
        temp = self._head
        while temp:
            print(temp._element, end='-->')
            temp = temp._next
        print()


if __name__ == '__main__':
    ls = LinkedStack()
    ls.push(10)
    ls.push(20)
    ls.push(30)
    ls.push(40)
    ls.display()
    ls.push(70)
    print('Top Element: ', ls.top())
    print('Popped: ', ls.pop())
    ls.display()
