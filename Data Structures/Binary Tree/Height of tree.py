"""
The height of a binary tree is the number of edges between the tree's root and its furthest leaf.

HackerRank: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        else:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)

    def print_in_order(self):
        """
        Left -> Root -> Right
        :return:
        """
        self._print_in_order(self.root)

    def _print_in_order(self, cur_node):
        if cur_node:
            self._print_in_order(cur_node.left)
            print(cur_node.data)
            self._print_in_order(cur_node.right)

    def height(self):
        """
        Calculate height of binary tree
        :return:
        """
        if self.root is None:
            return 0
        else:
            return self.__height(self.root) - 1

    def __height(self, cur_node):
        if cur_node:
            ldepth = self.__height(cur_node.left)
            rdepth = self.__height(cur_node.right)

            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1
        return 0


if __name__ == '__main__':
    root = BinarySearchTree()
    root.insert(3)
    root.insert(1)
    root.insert(7)
    root.insert(5)
    root.insert(4)
    root.print_in_order()
    print(root.height())
