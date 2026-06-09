class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        map = {} # val to Node

        for num in nums:
            if num in map:
                continue
            new_node = Node(num)
            map[num] = new_node
            if num - 1 in map:
                prev_node = map[num - 1]
                prev_node.next = new_node
            if num + 1 in map:
                next_node = map[num+1]
                new_node.next = next_node
        max_len = 1
        visited = set()
        for key, val in map.items():
            if key not in visited:
                visited.add(key)
                cur_len = 1
                cur_node = val
                while cur_node.next:
                    cur_len += 1
                    cur_node = cur_node.next
                    visited.add(cur_node.val)
                max_len = max(max_len, cur_len)
        return max_len


"""
[2,20,4,1,3,4,5]

1->2->3->4->5
20
"""
        