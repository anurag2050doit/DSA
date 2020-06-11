"""
Maximum width of a binary tree
Given a binary tree, write a function to get the maximum width of the given tree. Width of a tree is maximum of
widths of all levels.
Let us consider the below example tree.

         1
        /  \
       2    3
     /  \    \
    4    5     8
              /  \
             6    7
For the above tree,
width of level 1 is 1,
width of level 2 is 2,
width of level 3 is 3
width of level 4 is 2.



So the maximum width of the tree is 3
"""


class Node:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val


def getMaxWidth(root):
    if root is None:
        return 0
    if root.left is None:
        return -1
    if root.right is None:
        return 1
    lnode = min(getMaxWidth(root.left), getMaxWidth(root.left.left) - 1)
    rnode = max(getMaxWidth(root.right), getMaxWidth(root.right.right) + 1)

    return rnode - lnode


if __name__ == '__main__':
    node = Node(1)
    node.left = Node(2)
    node.left.left = Node(4)
    node.left.right = Node(5)

    node.right = Node(3)
    node.right.left = Node(8)
    # node.right.right = Node(9)
    node.right.left.left = Node(6)
    node.right.left.right = Node(7)

    print(getMaxWidth(node))
