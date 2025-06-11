class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        
        x=1
        y=2
        for i in range(3,n+1):
            
            z=x+y
            x=y
            y=z
        return y
            
