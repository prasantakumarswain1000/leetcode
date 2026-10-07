class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        new=[]
        for i in range(0,len(nums),2):
            new.append(nums[i+1])
            new.append(nums[i])
        return new 

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        