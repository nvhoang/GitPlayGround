# ### 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/
#     
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Note: Your solution should be in logarithmic time complexity.

# Runtime: 36 ms, faster than 75.87% of Python3 online submissions for Factorial Trailing Zeroes.
# Memory Usage: 14 MB, less than 10.00% of Python3 online submissions for Factorial Trailing Zeroes.

# In[ ]:


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Starting time: 3:55pm
        Ending time: 4:41pm
        """
        from math import floor, log
        if n < 5:
            return 0
        log5num = floor(log(n)/log(5))
        output = [n // (5**i) for i in range(log5num, 0, -1)]
        return sum(output)

 
                
            

