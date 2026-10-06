class Solution(object):
    def maximumWealth(self, accounts):
        welth=[]
        for  i in accounts:
            welth.append(sum(i))
        return max(welth)
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        