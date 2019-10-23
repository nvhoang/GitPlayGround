 
# ### 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/submissions/
# In this problem, a tree is an undirected graph that is connected and has no cycles.
# 
# The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
# 
# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.
# 
# Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.
# 
# Example 1:
# 
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3
# Example 2:
# 
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3
# Note:
# 
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

# Success
# Details 
# Runtime: 60 ms, faster than 95.29% of Python3 online submissions for Redundant Connection.
# Memory Usage: 14.3 MB, less than 14.29% of Python3 online submissions for Redundant Connection.
# 

# In[ ]:


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        3:42pm
        """
        from collections import defaultdict
        nodes = dict() # key: node, val: graph_id
        graphs = defaultdict(list) # key: graph_id, val: list of node that in this specific graph
        
        for edge in edges:
            u, v = edge
            graph_id_u = nodes.get(u, None)
            graph_id_v = nodes.get(v, None)
            if graph_id_u is None:
                if graph_id_v is None: # new graph initialized by u, v
                    graph_id = u # use u as the new graph_id
                    graphs[graph_id] = [u, v] 
                    nodes[u] = graph_id
                    nodes[v] = graph_id
                    #print('1-', graphs, nodes)
                else:# u is added into the graph in which v already is
                    graphs[graph_id_v].append(u)
                    nodes[u] = graph_id_v
                    #print('2-', graphs, nodes)
            else:
                if graph_id_v is None: #v is added into the graph in which u already is
                    graphs[graph_id_u].append(v)
                    nodes[v] = graph_id_u
                    #print('3-', graphs, nodes)
                else:
                    if graph_id_u == graph_id_v: #this edge makes a cycle
                        #print('4a-', graphs, nodes)
                        return edge
                    else:
                        for node_id in graphs[graph_id_v]:
                            nodes[node_id] = graph_id_u
                        graphs[graph_id_u].extend(graphs[graph_id_v])
                        graphs.pop(graph_id_v)
                        #print('4b-', graphs, nodes)
            
            
                
       
       