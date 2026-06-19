# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeTwoLists(head1, head2):
            dummy = ListNode()
            cur = dummy
            while head1 and head2:
                if head1.val <= head2.val:
                    cur.next = head1
                    head1 = head1.next
                else:
                    cur.next = head2
                    head2 = head2.next
                cur = cur.next
            cur.next = head1 or head2
            return dummy.next
        
        while len(lists) != 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    new_lists.append(mergeTwoLists(lists[i], lists[i + 1]))
                else:
                    new_lists.append(lists[i])
            lists = new_lists
        return lists[0]

"""
1 -> 2 -> 4
1 -> 3 -> 5
3 -> 6
"""