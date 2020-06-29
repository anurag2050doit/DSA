"""

Sample Input

1
5
1
2
3
4
5
Sample Output

5 4 3 2 1
Explanation

The initial linked list is: 1 -> 2 -> 3 -> 4 -> 5 -> NULL

The reversed linked list is: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
"""


def reverse(head):
    temp = head
    prev = None
    while temp:
        ne = temp.next
        temp.next = prev
        prev = temp
        temp = ne
    head = prev
    return head
