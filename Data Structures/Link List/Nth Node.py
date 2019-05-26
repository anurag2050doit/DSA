"""
 GetNth() function that takes a linked list and an integer index and returns the data value stored in the node at that index position.
"""


class Node:
    # Constructor to initial object
    # Create Node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    # Constructor for linklist
    def __init__(self):
        self.head = None

    def push(self, data):
        next_node = Node(data)
        next_node.next = self.head
        self.head = next_node

    def print_link_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def get_data_by_index(self, index):
        count = 0
        temp = self.head
        while temp:
            if count == index:
                return temp.data
            else:
                temp = temp.next
                count += 1
        raise IndexError

    def get_index_by_data(self, data):
        count = 0
        temp = self.head
        while temp:
            if temp.data == data:
                return count
            else:
                temp = temp.next
                count += 1
        return -1


if __name__ == '__main__':
    llist = LinkList()
    llist.push(3)
    llist.push(12)
    llist.push(33)
    llist.push(90)
    llist.push(6)
    llist.print_link_list()
    print(llist.get_data_by_index(3))
    print(llist.get_index_by_data(12))
