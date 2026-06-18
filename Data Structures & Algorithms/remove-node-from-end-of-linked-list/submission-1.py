# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        sz = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            sz += 2
        if fast: sz += 1

        if sz == 1: return None

        target_post = sz - n + 1

        if target_post == 1:
            return head.next
        cur = head
        prev = None

        while target_post:
            target_post -= 1
            if target_post == 0:

                prev.next = cur.next
                cur.next = None
                break
            prev = cur
            cur = cur.next
        return head
            


"""
length of linked list = m
nth element from the end = (m - n + 1)th element from the beginning

1,2,3,4,5
1,2,3,4
if odd, slow pointer ends up in the middle (m/2)th position
fast pointer at end of list
if even, slow pointer ends up in the (m/2 + 1)th position
fast pointer at None (out of bounds)
"""