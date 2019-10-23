# ### 952. Largest Component Size by Common Factor
# 
# https://leetcode.com/problems/largest-component-size-by-common-factor/
# 
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

# The following code is accepted by Leetcode. But it is the 3rd code that I have for this problem. 
# I also pasted the first two codes which seem run correctly but takes too long and 
# Leetcode returns a 'time out' message.

# In[ ]:


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        """
        
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
        
        prime_list = find_all_primes(max(A))
        
        max_cc = 0
        from collections import defaultdict
        cc = defaultdict(list) #prime_num_id (served as id for the cc): (list of 
        						#prime_factors in the connected component, total number of A[i] in this cc). 
        pfs = defaultdict(set) #prime_fractor: cc_id
        next_cc_id = 0
        for ai in A:
            pfs_i = find_prime_factors(ai, prime_list)
            cc_ids = list(set([pfs[pf_i] for pf_i in pfs_i if pfs.get(pf_i, None) is not None]))
            #print('--', pfs_i, cc_ids)
            if len(cc_ids) == 0: # new cc
                cc[next_cc_id] = (pfs_i, 1)
                for pf_i in pfs_i:
                    pfs[pf_i] = next_cc_id
                next_cc_id += 1
            else:
                cc_id = cc_ids[0]
                cc[cc_id] = (cc[cc_id][0].union(pfs_i), cc[cc_id][1] + 1)
                for pf_i in pfs_i:
                    pfs[pf_i] = cc_id
                for cc_id_j in cc_ids[1:]:
                    pfs_j, tot_j = cc.pop(cc_id_j)
                    #print(cc_id_j, pfs_j, tot_j, cc[cc_id])
                    cc[cc_id] = (cc[cc_id][0].union(pfs_j), cc[cc_id][1] + tot_j)
                    for pf in pfs_j:
                        pfs[pf] = cc_id
            #print(ai, pfs_i, cc_ids, cc, pfs)
                        
        for _, tot_k in cc.values():
            if max_cc < tot_k:
                max_cc = tot_k
                
        return max_cc
                    
      


# The following two codes probably run correctly but Leetcode returned "Time Limit Exceeded"

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
                
            
        
                
            

