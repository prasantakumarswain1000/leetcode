class Solution(object):
    def sortedSquares(self, nums):
        nums2 = []
        for i in nums:
            nums2.append(i * i)
        nums2.sort()
        return nums2