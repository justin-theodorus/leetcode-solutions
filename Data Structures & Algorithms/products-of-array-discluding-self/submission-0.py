class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        for num in nums:
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(prefix[-1] * num)
        postfix = []
        start = 1
        for i in range(len(nums) - 1, -1, -1):
            if not postfix:
                postfix.append(nums[i])
            else:
                postfix.append(postfix[-1] * nums[i])
        postfix.reverse()

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(postfix[1])
            elif i == len(nums) - 1:
                ans.append(prefix[-2])
            else:
                ans.append(prefix[i - 1] * postfix[i + 1])
        return ans


"""
 0 1 2 3
[2,5,6,7]
[5 * 6 * 7, 2 * 6 * 7, 2 * 5 * 7, 2 * 5 * 6]
[postfix[1], prefix[0] * postfix[2], prefix[1] * postfix[3], prefix[2]]

prefix = [2, 2 * 5, 2 * 5 * 6, 2 * 5 * 6 * 7]
postfix = [2 * 5 * 6 * 7, 5 * 6 * 7, 6 * 7, 7]
"""
        