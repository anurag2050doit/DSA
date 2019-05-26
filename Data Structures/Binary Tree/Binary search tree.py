"""
    The following is definition of Binary Search Tree(BST) according to Wikipedia

    Binary Search Tree, is a node-based binary tree data structure which has the following properties:
    The left subtree of a node contains only nodes with keys lesser than the node’s key.
    The right subtree of a node contains only nodes with keys greater than the node’s key.
    The left and right subtree each must also be a binary search tree.
    There must be no duplicate nodes.

GFG: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
"""


class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.value = val


class BinaryTree:
    # Constructor for Node Structure
    def __init__(self):
        self.root = None

    # Inserting data in tree
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)

        else:
            print('Value already present in Tree')

    def print_in_order(self):
        """
        Left -> Root -> Right
        :return:
        """
        self._print_in_order(self.root)

    def _print_in_order(self, cur_node):
        if cur_node:
            self._print_in_order(cur_node.left)
            print(cur_node.value)
            self._print_in_order(cur_node.right)

    def print_pre_order(self):
        """
        Root -> Left -> Right
        :return:
        """
        self._print_pre_order(self.root)

    def _print_pre_order(self, cur_node):
        if cur_node:
            print(cur_node.value)
            self._print_pre_order(cur_node.left)
            self._print_in_order(cur_node.right)

    def print_post_order(self):
        """
        Left -> Right -> Root
        :return:
        """
        self._print_post_order(self.root)

    def _print_post_order(self, cur_node):
        if cur_node:
            self._print_post_order(cur_node.left)
            self._print_post_order(cur_node.right)
            print(cur_node.value)


if __name__ == '__main__':
    root = BinaryTree()
    root.insert(2)
    root.insert(7)
    root.insert(5)
    root.insert(9)
    root.insert(1)
    root.insert(12)
    print('<<< In-order print >>>')
    root.print_in_order()
    print('\n <<< Pre-order print >>>')
    root.print_pre_order()
    print('\n <<< Post-order print >>>')
    root.print_post_order()
