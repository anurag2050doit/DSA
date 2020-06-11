"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

REF: https://leetcode.com/problems/add-two-numbers/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1 = self.list_to_digit(l1)
        number2 = self.list_to_digit(l2)
        sum_number = number1 + number2
        return self.digit_to_list(sum_number)

    @staticmethod
    def digit_to_list(number):
        head, next_node = None, None
        while True:
            digit = number % 10
            next_node = ListNode(digit)
            if head is None:
                head = next_node
            else:
                temp = head
                while temp.next:
                    temp = temp.next
                temp.next = next_node
            number = number // 10
            if number == 0:
                break
        return head

    @staticmethod
    def list_to_digit(link_list):
        head = link_list
        number = 0
        digit_value = 1
        while head is not None:
            value = head.val
            number = value * digit_value + number
            digit_value = digit_value * 10
            head = head.next
        return number


class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.lltoint(l1)
        num2 = self.lltoint(l2)
        sum_num = num1 + num2
        reverse_list = self.reverse_list(sum_num)
        result = self.inttoll(reverse_list)
        return result

    def inttoll(self, rv_list):
        next_node = None
        try:
            while True:
                val = rv_list.pop()
                next_node = ListNode(val, next_node)
        except:
            pass
        return next_node

    def reverse_list(self, sum_number):
        return list(reversed([x for x in str(sum_number)]))

    def lltoint(self, llist):
        val = int(llist.val)
        if isinstance(llist.next, ListNode):
            val = val + self.lltoint(llist.next) * 10
        return val


if __name__ == '__main__':
    obj = Solution()
    # Case 1:
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # Case 2:
    l1 = ListNode(0)
    l2 = ListNode(0)

    result = obj.addTwoNumbers(l1, l2)
    print(obj.list_to_digit(result))

    # Solution 2
    obj2 = Solution1()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = obj2.addTwoNumbers(l1, l2)
    print(obj2.lltoint(result))
