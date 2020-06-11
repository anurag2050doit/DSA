"""
Check if a given Binary Tree is Heap
Given a binary tree, we need to check it has heap property or not, Binary tree need to fulfill the following two
conditions for being a heap –

It should be a complete tree (i.e. all levels except last should be full).
Every node’s value should be greater than or equal to its child node (considering max-heap).
"""


class Heap:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.val == other.val

    def __ge__(self, other):
        return self.val >= other.val

    def __le__(self, other):
        return self.val <= other.val

    def count_nodes(self, root):
        """
        Counting Number of node present from root
        """
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

    def valid_bst(self, root):
        """
        Verify if its a valid binary search tree or not.
        """

        if root.left is None and root.right is None:
            # Case: If left and right both are null
            return True

        if root.right is None:
            # Case: If right in null value of root node should be greater than left node
            return root >= root.left
        else:
            # Case: If right and left both are not null
            # Value root node should be greater than right and left both
            if root >= root.left and root >= root.right:
                return self.valid_bst(root.left) and self.valid_bst(root.right)
            else:
                return False

    def complete_tree(self, root, index, node_count):

        if root is None:
            return True
        if index >= node_count:
            # Check maximum node
            return False

        return self.complete_tree(root.left, 2 * index + 1, node_count) and self.complete_tree(
            root.right, 2 * index + 2, node_count)

    def check_heap(self, root):
        node_count = self.count_nodes(root)
        if self.valid_bst(root) and self.complete_tree(root, 0, node_count):
            return True
        return False


if __name__ == '__main__':
    root = Heap(15)
    root.left = Heap(12)
    root.right = Heap(13)
    root.left.right = Heap(10)
    root.left.left = Heap(9)
    root.left.left.left = Heap(5)
    root.left.left.right = Heap(6)

    root = Heap(97)
    root.left = Heap(46)
    root.right = Heap(37)
    root.left.left = Heap(12)
    root.left.right = Heap(3)
    root.left.left.left = Heap(6)
    root.left.left.right = Heap(9)

    root.right.left = Heap(37)
    root.right.right = Heap(5)

    print(root.check_heap(root))
