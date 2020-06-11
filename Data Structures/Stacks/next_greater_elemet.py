"""
Next Greater Element
Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is
the first greater element on the right side of x in array. Elements for which no greater element exist, consider next
greater element as -1.

Examples:

For any array, rightmost element always has next greater element as -1.
For an array which is sorted in decreasing order, all elements have next greater element as -1.
For the input array [4, 5, 2, 25}, the next greater elements for each element are as follows.

Element       NGE
   4      -->   5
   5      -->   25
   2      -->   25
   25     -->   -1
d) For the input array [13, 7, 6, 12}, the next greater elements for each element are as follows.


  Element        NGE
   13      -->    -1
   7       -->     12
   6       -->     12
   12      -->     -1
"""


class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()

    def last(self):
        if not self.isEmpty():
            return self.data[-1]

    def isEmpty(self):
        return not self.data


class Solution:

    def right_highest(self, input_array):
        stack = Stack()
        for element in input_array:
            if not stack.isEmpty():
                last_stack_element = stack.last()
                while last_stack_element and last_stack_element < element:
                    print('{} -- {}'.format(last_stack_element, element))
                    stack.pop()
                    last_stack_element = stack.last()
            stack.push(element)

        while not stack.isEmpty():
            print('{} -- {}'.format(stack.pop(), '-1'))


if __name__ == '__main__':
    obj = Solution()
    obj.right_highest([4, 5, 2, 25])
