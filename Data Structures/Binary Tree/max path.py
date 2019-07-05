"""
Given a binary tree in which each node element contains a number. Find the maximum possible sum from one leaf node to
another.
The maximum sum path may or may not go through root. For example, in the following binary tree, the maximum sum is
27(3 + 6 + 9 + 0 – 1 + 10). Expected time complexity is O(n).

GFG: https://www.geeksforgeeks.org/find-maximum-path-sum-two-leaves-binary-tree/
"""

from sys import maxsize


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_path_sum_util(root_node, res):
    if root_node is None:
        return 0

    if root_node.left is None and root_node.right is None:
        return root_node.data

    ls = max_path_sum_util(root_node.left, res)
    rs = max_path_sum_util(root_node.right, res)

    # If both right and lift node is present
    if root_node.left is not None and root_node.right is not None:
        res[0] = max(res[0], ls + rs + root_node.data)

        return max(ls, rs) + root_node.data

    if root_node.left is None:
        return rs + root_node.data
    else:
        return ls + root_node.data


def max_path_sum(tree_node):
    res = [-maxsize]
    max_path_sum_util(tree_node, res)
    return res[0]


if __name__ == '__main__':
    root = Node(-15)
    root.left = Node(5)
    root.right = Node(6)
    root.left.left = Node(-8)
    root.left.right = Node(1)
    root.left.left.left = Node(2)
    root.left.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(9)
    root.right.right.right = Node(0)
    root.right.right.right.left = Node(4)
    root.right.right.right.right = Node(-1)
    root.right.right.right.right.left = Node(10)
    print(max_path_sum(root))
