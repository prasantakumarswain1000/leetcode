class Solution(object):
    def singleNumber(self, nums):
        hash_map={}
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        
        for i in nums :
            if hash_map[i]==1:
                return i
        

        """
        :type nums: List[int]
        :rtype: int
        """
        