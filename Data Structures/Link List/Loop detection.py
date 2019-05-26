"""
    Given a linked list, check if the the linked list has loop or not
"""


# Method 1: Hashing


class Node:
    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Inserting data into linklist
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_link_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Create Loop Link List
    def loop_link_list(self, pos):
        """
        1) Traverse the first linked list till k-th point
        2) Make backup of the k-th node
        3) Traverse the linked linked list till end
        4) Attach the last node with k-th node
        """
        count = 0
        temp = self.head
        loop_node = None
        while temp:
            if pos == count:
                loop_node = temp
            else:
                count += 1
            temp = temp.next
        temp.next = loop_node
        return temp

    # Using hash
    def detect_using_hash(self):
        list_hash = set()
        temp = self.head
        while temp:
            if temp in list_hash:
                return True
            else:
                list_hash.add(temp)
            temp = temp.next
        return False

    # Floyd’s Cycle-Finding Algorithm
    def detect_using_algo(self):
        single_step = self.head
        double_step = self.head
        while single_step and double_step and double_step.next:
            single_step = single_step.next
            double_step = double_step.next.next
            if single_step == double_step:
                return True
        return False


if __name__ == '__main__':
    llist = LinkList()
    llist.push(5)
    llist.push(10)
    llist.push(15)
    llist.push(3)
    llist.push(2)
    llist.print_link_list()
    print(llist.detect_using_hash())
    print(llist.detect_using_algo())
    llist.loop_link_list(3)
