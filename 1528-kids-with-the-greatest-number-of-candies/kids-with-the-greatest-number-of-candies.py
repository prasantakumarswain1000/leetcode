class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans=[]
        for x in candies:
            ans.append(x+extraCandies>=max(candies))
        return ans 
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        