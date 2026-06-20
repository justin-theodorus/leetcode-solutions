from typing import List
from sortedcontainers import SortedSet


def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:
    for num1 in nums1:
        sorted_set.add(num1)
    for num2 in nums2:
        sorted_set.discard(num2)
    ans = []
    for i in range(3):
        ans.append(sorted_set.pop(0))
    return ans


# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
