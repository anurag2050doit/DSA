""""
Given a Binary Tree, find the vertical sum of the nodes that are in the same vertical line. Print all sums through
different vertical lines.
Examples:

      1
    /   \
  2      3
 / \    / \
4   5  6   7
The tree has 5 vertical lines



Vertical-Line-1 has only one node 4 => vertical sum is 4
Vertical-Line-2: has only one node 2=> vertical sum is 2
Vertical-Line-3: has three nodes: 1,5,6 => vertical sum is 1+5+6 = 12
Vertical-Line-4: has only one node 3 => vertical sum is 3
Vertical-Line-5: has only one node 7 => vertical sum is 7

So expected output is 4, 2, 12, 3 and 7

GFG: https://www.geeksforgeeks.org/vertical-sum-in-a-given-binary-tree/
"""


class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val


vertical_sum_map = {}


def vertical_sum(tree, pointer=0):
    if tree:
        vertical_sum_map[pointer] = vertical_sum_map.get(pointer, 0) + tree.val
    if tree.left:
        cursor = pointer - 1
        vertical_sum(tree.left, cursor)
    if tree.right:
        cursor = pointer + 1
        vertical_sum(tree.right, cursor)
    return vertical_sum_map


if __name__ == '__main__':
    # node = Node(1)
    # node.left = Node(2)
    # node.left.left = Node(4)
    # node.left.right = Node(5)
    #
    # node.right = Node(3)
    # node.right.left = Node(7)
    # node.right.right = Node(6)
    #
    # print(vertical_sum(node))

    node = Node(1)
    node.left = Node(2)
    node.left.left = Node(4)
    node.left.right = Node(5)

    node.right = Node(3)
    node.right.left = Node(6)
    node.right.right = Node(7)

    print(vertical_sum(node))
