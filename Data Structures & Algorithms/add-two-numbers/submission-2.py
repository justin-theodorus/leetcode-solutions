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
        while cur1 or cur2 or extra:
            v1 = cur1.val if cur1 else 0
            v2 = cur2.val if cur2 else 0

            new_val = v1 + v2 + extra
            extra = new_val // 10
            new_val = new_val % 10
            cur.next = ListNode(new_val)

            cur = cur.next
            cur1 = cur1.next if cur1 else None
            cur2 = cur2.next if cur2 else None
            
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