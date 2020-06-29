

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    t1 = head
    t2 = head
    pos = positionFromTail
    while pos > 0:
        t2 = t2.next
        pos -= 1
    while t2.next:
        t2 = t2.next
        t1 = t1.next
    return t1.data

