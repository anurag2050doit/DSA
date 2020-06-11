"""
Convert a given Binary Tree to Doubly Linked List
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to
be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder
of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.
"""


class DoubleLLNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class TrueNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


class Solution:

    def __init__(self):
        self.head = None
        self.tail = None

    def in_order_convert(self, root):
        """
        Left -> Root -> Right
        """
        if root is None:
            return
        self.in_order_convert(root.left)
        dll = DoubleLLNode(root.val)
        if not self.head:
            self.head = dll
            self.tail = self.head
        else:
            self.tail.next = dll
            dll.prev = self.tail
            self.tail = dll
        self.in_order_convert(root.right)

    def pre_order_covert(self, root):
        """
        Root -> Left -> Right
        """
        if root is None:
            return
        dll = DoubleLLNode(root.val)
        if not self.head:
            self.head = dll
            self.tail = self.head
        else:
            self.tail.next = dll
            dll.prev = self.tail
            self.tail = dll
        self.pre_order_covert(root.left)
        self.pre_order_covert(root.right)

    def post_order_covert(self, root):
        """
        Left -> Right -> Root
        """
        if root is None:
            return
        self.pre_order_covert(root.left)
        self.pre_order_covert(root.right)
        dll = DoubleLLNode(root.val)
        if not self.head:
            self.head = dll
            self.tail = self.head
        else:
            self.tail.next = dll
            dll.prev = self.tail
            self.tail = dll

    def print_dll(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next


if __name__ == '__main__':
    tree = TrueNode(10)
    tree.left = TrueNode(12)
    tree.left.left = TrueNode(25)
    tree.left.right = TrueNode(30)
    tree.right = TrueNode(15)
    tree.right.left = TrueNode(36)

    obj = Solution()
    obj.in_order_convert(tree)
    print('<<< In-order print >>>')
    obj.print_dll()
    print('\n <<< Pre-order print >>>')
    obj.head = None
    obj.pre_order_covert(tree)
    obj.print_dll()
    print('\n <<< Post-order print >>>')
    obj.head = None
    obj.post_order_covert(tree)
    obj.print_dll()
