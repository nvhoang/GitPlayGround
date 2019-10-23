#!/usr/bin/env python
# coding: utf-8

# In[1]:


def decode_string_recursive(input):
    """
    Test cases:
    decode_string_recursive('abc2')
    decode_string_recursive('abc2[ui]')
    decode_string_recursive('abc2e[ui]')
    decode_string_recursive('abc2[ui]jk3[op]')
    decode_string_recursive('abc2[ui]3[op]')

    decode_string_recursive('[ui]jk3[op]')
    decode_string_recursive('1[ui]jk3[op]')
    decode_string_recursive('1[ui]jk3[op3]9')
    decode_string_recursive('1[ui]jk3[op3r]9')

    decode_string_recursive('abc2[de3[08]3]')
    decode_string_recursive('abc2[de3[08i]3g]')

    decode_string_recursive('abc2[de3[08i]3g]_3[tea1[pot]]__')
    """
    def decode_string(input, i=0):
        """
        Assuming there is no illegitimate '[' or ']'.
        Assuming if there is no digit right before '[...]' then the content of the bracket will be remove (rep = 0)
        Scanning each character in input.
        - If the character is not a number or a '[' or ']', then add it to the output
        - If the character is a number digit, then store the digit into a buffer for number digits num_buf
            + if the last number digit is not followed by an '[', the content of num_buf is added into output
            + if it is followed by an '[', its value is the repetition value
        - 
        """
        n = len(input)
        if n == 0:
            return ''
        num_buf, output = '', ''
        while i < n:
            c = input[i]
            if (c < '0' or c > '9') and c != '[' and c != ']': #if it is not a number or a '[' or ']'
                if num_buf != '': # if the last number digit is not followed by an '['
                    output += num_buf
                    num_buf = ''
                output += c
                i += 1 # increase i to move to the next character 
            elif c == '[':
                # all the digit right before the '[' makes up the repetition time
                if num_buf != '':
                    rep = int(num_buf)
                else:
                    rep = 0 # if there is no number before the '[', repetition time = 0, i.e., deleting '[...]'
                num_buf = '' # reset to '' after the digits in the num_buf are translated into repetition time
                             # to avoid num_buf content will be added into output
                bracket_content, i = decode_string(input, i+1) # Recursively call the function for input[i+1:]
                                                               # Content between this open '[' and its corresponding
                                                               # ']' will be return in bracket_content
                                                               # The returned i value reflects the remaining
                                                               # of the string right after the ']'
                                                               
                output += bracket_content * rep
            elif c == ']':
                # if there are digits right before ']', they needed to be added into the output
                if num_buf != '':
                    output += num_buf
                # the ']' signifies the end of the content in the current '[...]', need to return the content
                # inside '[...]' and the index of the beginning of the remaining string
                return output, i + 1
            else:# if c is a digit, add c into a digit buffer:
                num_buf += c
                i += 1 # increase i to move to the next character 
        return output + num_buf, i
    output, _ = decode_string(input)
    return output


# In[2]:


decode_string_recursive('abc2[de3[08i]3g]_3[tea1[pot]]__')


# In[ ]:




