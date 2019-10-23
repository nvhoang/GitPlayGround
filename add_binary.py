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
        


