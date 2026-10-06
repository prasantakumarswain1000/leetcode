class Solution(object):
    def runningSum(self, nums):
        new_list=[nums[0]]
        for i in range(len(nums)-1):
            
            nums[i]=nums[i]+nums[i+1]
            nums[i+1]=nums[i]
            new_list.append(nums[i])
        
         
        return new_list
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        