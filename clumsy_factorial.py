
# ### 1006. Clumsy Factorial
# https://leetcode.com/problems/clumsy-factorial/submissions/
# Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
# 
# We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.
# 
# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.
# 
# Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.
# 
# Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.
# 
#  
# 
# Example 1:
# 
# Input: 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1
# Example 2:
# 
# Input: 10
# Output: 12
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
#  
# 
# Note:
# 1 <= N <= 10000
# -2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)

# Success
# Details 
# Runtime: 92 ms, faster than 34.65% of Python3 online submissions for Clumsy Factorial.
# Memory Usage: 13.8 MB, less than 42.86% of Python3 online submissions for Clumsy Factorial.

# In[ ]:


class Solution:
    def clumsy(self, N: int) -> int:
        """
        Starting time: 3:25pm
        Finishing time:  3:51pm
        """
        from math import floor
        output = [N]
        for i in range(N-1, 0, -1):
            if (N - i) % 4 == 1:
                output[-1] *= i
            elif (N - i) % 4 == 2:
                output[-1] = floor(output[-1]/i) if output[-1] > 0 else -floor(abs(output[-1])/i)
            elif (N - i) % 4 == 3:
                output.append(i)
            elif (N - i) % 4 == 0:
                output.append(-i)
                
        return sum(output)
            
