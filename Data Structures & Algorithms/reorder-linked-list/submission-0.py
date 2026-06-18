# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # combine both halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
"""
need head and tail

2 -> 4 -> 6 -> 8 -> 10

2 -> 4 -> 6
8 -> 10

2 -> 4 -> 6
10 -> 8

2 -> 10 -> 4 -> 8 -> 6
------------------------------
2 -> 4 -> 6 -> 8

2 -> 4
6 -> 8

2 -> 4
8 -> 6

2 -> 8 -> 4 -> 6
"""