"""
Sample Input

3
16
13
7
1
2
Sample Output

16 13 1 7
Explanation

The initial linked list is 16 13 7. We have to insert  at the position  which currently has  in it. The updated linked list will be 16 13 1 7


"""

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    temp = head
    prev = head
    while temp.next and position > 0:
        prev = temp
        temp = temp.next
        position -= 1
    new_node.next = temp
    prev.next = new_node
    return head


