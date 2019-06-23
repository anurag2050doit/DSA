"""
Check for balanced parentheses in an expression

Given an expression string exp , write a program to examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]”
are correct in exp. For example, the program should print true for exp = “[()]{}{[()()]()}” and false for exp = “[(])”

GFG: https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
"""


class NotOpenParentheses(Exception):
    pass


class OrderMisMatch(Exception):
    pass


class ArrayStack:
    parentheses_map = {')': '(', ']': '[', '}': '{'}

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, element):
        self._data.append(element)

    def pop(self, element):
        if self.is_empty():
            raise NotOpenParentheses('No open parentheses found: ', element)
        if self.top() != self.parentheses_map[element]:
            raise OrderMisMatch('Expected to close: ', self.top(), 'before closing: ', element)
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise NotOpenParentheses('Stack is empty')
        return self._data[-1]


def check_parentheses(expression):
    open_parentheses = ['(', '[', '{']
    close_parenthese = [')', ']', '}']
    stack = ArrayStack()
    try:
        for l in expression:
            if l in open_parentheses:
                stack.push(l)
            elif l in close_parenthese:
                stack.pop(l)
    except OrderMisMatch:
        return 'Parentheses are imperfectly close'
    except NotOpenParentheses:
        return 'Parentheses are imperfectly close'

    if stack.is_empty():
        return 'Parentheses are perfectly closed'


if __name__ == '__main__':
    expr = "{()}[]"
    print(check_parentheses(expr))
    expr = "[(])"
    print(check_parentheses(expr))
    expr = "2 + (2+2)*{21(3+)}]"
    print(check_parentheses(expr))
