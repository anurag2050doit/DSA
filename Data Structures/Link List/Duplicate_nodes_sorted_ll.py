"""
Delete duplicate-value nodes from a sorted linked list

Sample Input

1
5
1
2
2
3
4
Sample Output

1 2 3 4
Explanation

The initial linked list is: 1 -> 2 -> 2 -> 3 -> 4 -> NULL

The final linked list is: 1 -> 2 -> 3 -> 4 -> NULL
"""


# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    temp = head
    if temp is None:
        return
    while temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next

        else:
            temp = temp.next
    return head




