"""
Find the middle of a given linked list

Given a singly linked list, find middle of the linked list. For example, if given linked list is 1->2->3->4->5 then output should be 3.

If there are even nodes, then there would be two middle nodes, we need to print second middle element. For example, if given linked list is 1->2->3->4->5->6 then output should be 4.

GFG: https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def find_middle_node(self):
        """
        Traversing through the Link List with two pointer one with single step and other with double step
        If double finish the Link List it means single has travelled half only.
        :return:
        """
        single_step = self.head
        double_step = self.head

        while double_step and double_step.next:
            single_step = single_step.next
            double_step = double_step.next.next

        return single_step.data


if __name__ == '__main__':
    llist = LinkList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    middle = llist.find_middle_node()
    print(middle)
