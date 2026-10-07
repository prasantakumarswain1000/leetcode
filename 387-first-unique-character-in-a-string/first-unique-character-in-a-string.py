class Solution(object):
    def firstUniqChar(self, s):
        hash_map={}
        for i in s :
            hash_map[i]=hash_map.get(i,0)+1
        for index,value in enumerate(s):
            if hash_map[value]==1:
                return index
        return -1

        """
        :type s: str
        :rtype: int
        """
        