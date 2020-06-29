"""
Sample Input

2
2
1
2
1
1
2
1
2
2
1
2
Sample Output

0
1
Explanation

In the first case, linked lists are: 1 -> 2 -> NULL and 1 -> NULL

In the second case, linked lists are: 1 -> 2 -> NULL and 1 -> 2 -> NULL
"""



# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    t1 = llist1
    t2 = llist2
    while t1 and t2:
        if t1.data != t2.data:
            return 0
        t1 = t1.next
        t2 = t2.next
        if (t1 and t2== None) or (t2 and t1== None):
            return 0
    return 1


