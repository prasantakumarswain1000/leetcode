class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False

        original=x
        total_sum=0
        while x>0:
            total_sum=(total_sum*10)+(x%10)
            x=x//10
        return total_sum==original
        
        """
        :type x: int
        :rtype: bool
        """
        