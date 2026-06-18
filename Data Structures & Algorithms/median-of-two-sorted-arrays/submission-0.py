class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # decrease left partition for nums1
                r = i - 1
            else:
                # Bleft > Aright
                # increase left partition for nums1
                # decrease left partition for nums2
                l = i + 1



"""
[1,2,3,4,5,6,7]
[1,2,3,4]
for odds: we want the total_len // 2 element
for evens: we want the total_len // 2 - 1 and total_len // 2 elements

left and right partitions of nums1 and nums2

valid if the biggest element in the left partition is smaller than the
smallest element in the right partition (nums1 compare with nums 2, vice versa)

if nums1_left > nums2_right, decrease left partition for nums1

if nums2_left > nums1_right, increase left partition for nums 1 (decrease left partition
for nums 2)

left partition of both must sum to half
"""

