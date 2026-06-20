# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseK(self, head, prev, k):
        cur_prev = None
        tail = head
        cur = head
        while cur and k:
            k -= 1
            tmp = cur.next
            cur.next = cur_prev
            cur_prev = cur
            if k == 0 or not tmp:
                prev.next = cur
                break
            cur = tmp
        return tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        cur_head = head
        while cur_head:
            rev_head = cur_head
            # move cur_head by k steps
            count = k
            while count:
                if not cur_head:
                    return dummy.next
                cur_head = cur_head.next
                count -= 1
            
            # reverse first k nodes
            tail = self.reverseK(rev_head, prev, k)

            tail.next = cur_head
            prev = tail
        return dummy.next

"""
s         e    n
1 -> 2 -> 3 -> 4 -> 5 -> 6
2    1    0

1 -> 2 -> 3
<- 1 <- 2 <- 3

3 -> 2 -> 1 ->
4 -> 5 -> 6

move the cur_head by k
    if cur_head == None before k steps, return
reverse function that returns tail
connect the tail to cur_head
repeat


ch <- 1 <- 2 <- 3 <- p
p
    rh
                    ch
d -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
d -> 3 -> 2 -> 1 -> 4 -> 5 -> 6
               p
"""