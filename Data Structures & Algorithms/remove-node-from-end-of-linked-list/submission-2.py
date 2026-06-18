# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        l = dummy
        r = head

        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next
            


"""
length of linked list = m
nth element from the end = (m - n + 1)th element from the beginning

1,2,3,4,5
1,2,3,4
if odd, slow pointer ends up in the middle (m/2)th position
fast pointer at end of list
if even, slow pointer ends up in the (m/2 + 1)th position
fast pointer at None (out of bounds)

set a left and right pointer of distance n
when r is null, l.next is the Node we want to remove

d,1,2,3,4,5
l   r
"""