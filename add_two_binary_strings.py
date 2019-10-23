#!/usr/bin/env python
# coding: utf-8

# ### 67. Add Binary
# 
# https://leetcode.com/problems/add-binary/
# 
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# 
# Input: a = "1010", b = "1011"
# Output: "10101"

# In[18]:


# swap a, and b so that a is always the shorter length string
# reversed bit order in each string
def add_two_bin_strings(a, b):
    class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else: 
            a = '0' * (len(b) - len(a)) + a
        carry = '0'
        output = ''
        for d1, d2 in zip(a[::-1], b[::-1]):
            if (d1 == '0' and d2 == '1') or (d1 == '1' and d2 == '0'):
                if carry == '0':
                    output += '1'
                else:
                    output += '0'
            elif d1 == '0' and d2 == '0':
                output += carry
                carry = '0'
            else: # d1 == '1' and d2 == '1':
                output += carry
                carry = '1'
        if carry == '1':
            output = carry + output[::-1]
        else:
            output = output[::-1]
        return output
        


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
            
        
        


# ### 952. Largest Component Size by Common Factor
# 
# https://leetcode.com/problems/largest-component-size-by-common-factor/solution/
# Given a non-empty array of unique positive integers A, consider the following graph:
# 
# There are A.length nodes, labelled A[0] to A[A.length - 1];
# There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.
# 
#  
# 
# Example 1:
# 
# Input: [4,6,15,35]
# Output: 4
# 
# Example 2:
# 
# Input: [20,50,9,63]
# Output: 2
# 

# Time Limit Exceeded

# In[ ]:


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        """
        Time: 45'
        The code run slows, but probably is correct (Leecode return a "Time Limit Exceeded" error)
        Build a graph includes:
        - Nodes: A[i]
        - edges between node i and j: if A[i] and A[j] has common factor greater than 1
        
        Use Breadth First Search to find all strong connected components
        """
        def common_factor(a, b):
            if a > b:
                a, b = b, a # a is the smallest of the two
            if a == 1:
                return 1
            if a == b:
                return a
            return common_factor(a, b-a)
        
        
        def check_connection(id1, id2):
            return common_factor(A[id1], A[id2]) != 1
        
        
        from collections import defaultdict
        n = len(A)
        edges = defaultdict(list)
        for id1 in range(n):
            for id2 in range(id1 + 1, n):
                if check_connection(id1, id2):
                    edges[id1].append(id2)
                    edges[id2].append(id1)
        #print(edges)
        connected_components = [] #list of connected components each of which is a list
                                 # of members' node id
        
        unexplored = [True for _ in range(n)]
        for u in range(n):
            if unexplored[u]:
                unexplored[u] = False
                q = [u]
                connected_components.append([u])
                while q:
                    curr_node = q.pop(0)
                    for v in edges[curr_node]:
                        if unexplored[v]:
                            unexplored[v] = False
                            q.append(v)
                            connected_components[-1].append(v)
                            
        return max([len(component) for component in connected_components])
                    
                
            


# In[ ]:


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        """
        Time: 45'
        The code run slows, but probably is correct (Leecode return a "Time Limit Exceeded" error)
        
        Each A[i] is decompose into a list of its prime factors.
        If its prime factors has overlap (intersection is not empty) with prime factors of already-exisitng cc,
        then they are joined.
        """
        def find_all_primes(n):
            """
            Find all the prime that are smaller than n
            """
            import numpy as np
            N = n + 1
            primes = np.array([True for _ in range(N)])
            primes[0:2] = False # primes[0], primes[1]: corresponding to 0 & 1 
                                # --> not a greater-than-1 prime
            #primes[2]: the first greater-than-1 prime
            primes[2*2::2] = False # set all multiple of 2 not a prime factor
            p = 3
            while p <= n:
                if primes[p]:
                    primes[p**2::p] = False
                p += 2
            return [i for i in range(N) if primes[i]]
        
        def find_prime_factors(n, primes):
            prime_factors = []
            for p in primes:
                if p * p > n:
                    break
                count = 0
                while n % p == 0:
                    n //= p
                    count += 1
                if count != 0:
                    prime_factors.append(p)
            if n != 1:
                prime_factors.append(n)
            return set(prime_factors)
        
        max_cc = 0
        primes = find_all_primes(max(A))
        connected_components = dict()
        for idx, a in enumerate(A):
            idx_a = set([idx])
            pf_a = find_prime_factors(a, primes)
            #print('_', pf_a)
            join = []
            for cc, pf_members in connected_components.items():
                pf_cc, members_cc = pf_members
                if len(pf_a.intersection(pf_cc)) != 0: 
                    pf_a = pf_a.union(pf_cc)
                    #print('--', idx_a, '--', members_cc)
                    idx_a = idx_a.union(members_cc)
                    join.append(cc)
                    #print('++', idx_a, members_cc)
            
            for cc in join:
                connected_components.pop(cc)
            connected_components[idx] = (pf_a, idx_a)
            if len(idx_a) >= max_cc:
                max_cc = len(idx_a)
            
        return max_cc
                
            
        
                
            

