# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = dummy
        cur1 = l1
        cur2 = l2

        extra = 0
        while cur1 and cur2:
            total = cur1.val + cur2.val + extra
            extra = 0
            while total >= 10:
                extra += 1
                total -= 10
            cur.next = ListNode(total)
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next
        
        while cur1:
            total = cur1.val + extra
            extra = 0
            while total >= 10:
                extra += 1
                total -= 10
            cur.next = ListNode(total)
            cur = cur.next
            cur1 = cur1.next
        
        while cur2:
            total = cur2.val + extra
            extra = 0
            while total >= 10:
                extra += 1
                total -= 10
            cur.next = ListNode(total)
            cur = cur.next
            cur2 = cur2.next
        
        if extra != 0:
            cur.next = ListNode(extra)
        return dummy.next

        
        
            
            

"""
l1 = [1,2,3], l2 = [4,5,6]

321 + 654 = 975
[9,7,5]

17 + 29 = 46

7 -> 1 ->
9 -> 2 ->
6 -> 4 ->

17 + 1235 = 1252

[7, 1]
[2]

7 -> 1 ->
         l
5 -> 3 -> 2 -> 1 ->
               r

2 -> 5 -> 2 -> 1


9 -> 9 -> 9 ->
9 -> 9 -> 9 -> 9 -> 9 ->

8 -> 9 -> 9 -> 0 -> 0 -> 1
"""