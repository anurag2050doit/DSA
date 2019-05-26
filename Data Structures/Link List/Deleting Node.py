"""
Linked List | Deleting a node


GFG: https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
GFG: https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, value):
        # If LinkList is empty
        if not self.head:
            print('LinkList is empty')
        temp = self.head
        prev = self.head

        # If head itself contains value
        if temp.data == value:
            self.head = temp.next
            return

        # When value is in between linklist
        while temp:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next

        prev.next = temp.next

    def delete_by_index(self, index):
        # If LinkList is empty
        if not self.head:
            print('LinkList is empty')
        temp = self.head
        prev = self.head
        count = 0  # Assuming LinkList indexing form 0

        # If 0 index itself contains value
        if count == index:
            self.head = temp.next
            return

        # When index is in between Linklist
        while temp:
            if count == index:
                break
            prev = temp
            temp = temp.next
            count += 1

        prev.next = temp.next

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkList()
    llist.push(2)
    llist.push(23)
    llist.push(21)
    llist.push(9)
    llist.push(2312)
    llist.push(83)
    llist.push(93)
    print('<<< LinkList Before Deleting >>>')
    llist.print()
    llist.delete_by_value(9)
    print('<<< LinkList After Deleting >>>')
    llist.print()
    print('<<< LinkList Before Deleting >>>')
    llist.print()
    llist.delete_by_index(3)
    print('<<< LinkList After Deleting >>>')
