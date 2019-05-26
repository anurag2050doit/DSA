"""
Inserting a node to LinkList
"""


class Node:
    """
    Each node contain data and pointer to next value
    """

    def __init__(self, data):
        self.next = None
        self.data = data


class LinkList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        """
        Adding element at fist node. New value is our first node
        :param new_value: data
        :return:
        """
        next_node = Node(new_value)
        next_node.next = self.head
        self.head = next_node

    def append(self, new_value):
        """
        Adding value to last node. Last node will be having new value
        :param new_value: data
        :return:
        """
        # Check if LinkList is empty
        if not self.head:
            self.push(new_value)
        else:
            # Get to last node and add new node
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(new_value)

    def insert_by_value(self, new_value, previous_value=None):
        """
        Inserting value in after previous value
        :param new_value: data
        :param previous_value: previous node
        :return:
        """
        # Check if LinkList is empty
        if not self.head:
            self.push(new_value)

        # If no previous value push at start
        if not previous_value:
            self.push(new_value)

        # Find the previous_value
        previous_node, next_node = self.find_by_value(previous_value)
        if previous_node != -1:
            previous_node.next = Node(new_value)
            previous_node.next.next = next_node
        else:
            # If value is not found append at last
            self.append(new_value)

    def insert_by_index(self, new_value, index_value=None):
        """
        We are considering index of LinkList is starting from zero
        Because in actual there is no index in LinkList
        :param new_value: data
        :param index_value: index at which value need to be inserted
        :return:
        """
        # Check if LinkList is empty
        if not self.head:
            self.push(new_value)

        # If no previous index push at last
        if not index_value:
            self.append(new_value)

        # Find the index node
        previous_node, next_node = self.find_by_index(index_value)
        if previous_node != -1:
            previous_node.next = Node(new_value)
            previous_node.next.next = next_node
        else:
            # If index is not found push at start
            self.push(new_value)

    def find_by_index(self, index):
        """
        Find node by it's Index
        :param index: position of node
        :return:
        """
        temp = self.head
        count = 0
        while temp:
            if count == index:
                return temp, temp.next
            count += 1
            temp = temp.next
        return -1, None

    def find_by_value(self, node_value):
        """
        Find a node which has lookup value
        :param node_value: lookup value
        :return:
        """
        temp = self.head
        while temp.next:
            if temp.data == node_value:
                return temp, temp.next
            temp = temp.next
        return -1, None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkList()
    llist.push(2)
    llist.push(2312)
    llist.push(83)
    llist.push(93)
    llist.push(32)
    llist.append(923)
    llist.append(932)
    llist.append(65)
    print('<<<Before Inserting by value>>')
    llist.print()
    llist.insert_by_value(732, 83)
    print('<<<After Inserting by value>>')
    llist.print()
    print('<<<Before Inserting by index>>')
    llist.insert_by_index(972, 4)
    print('<<<After Inserting by index>>')
    llist.print()
