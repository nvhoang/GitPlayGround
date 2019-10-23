
# ### 823. Binary Trees With Factors
# 
# https://leetcode.com/problems/binary-trees-with-factors/
# 
# Given an array of unique integers, each integer is strictly greater than 1.
# 
# We make a binary tree using these integers and each number may be used for any number of times.
# 
# Each non-leaf node's value should be equal to the product of the values of it's children.
# 
# How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

# Success
# Details 
# Runtime: 788 ms, faster than 22.22% of Python3 online submissions for Binary Trees With Factors.
# Memory Usage: 13.9 MB, less than 50.00% of Python3 online submissions for Binary Trees With Factors.

# In[ ]:


class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        """
        Starting time: 4:55pm
        Ending` time: 5:22pm
        """
        def find_subtrees(subA, a, output):
            for child1 in subA:
                child2 = a / child1
                if output.get(child2, None):
                    output[a] += output[child1] * output[child2]  
            return output
            
        A = sorted(A)
        output = {a: 1 for a in A} #the number of tree that has the num 'a' as root
        # the smallest num can be the root of one valid tree only as its cannot be the
        # product of the values of its children
        for i in range(1, len(A)):
            a = A[i]
            output = find_subtrees(A[:i], a, output)
        #print(output)
        return sum(output.values()) % (10**9 + 7)
            
 