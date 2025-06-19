"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {} #key is original node, value is new node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Base case: if the node deosn't exist
        if not node:
            return
        
        # Base case: if we've already visited the node
        if node in self.visited:
            return self.visited[node]
        
        # Create the new node and add the old node to visited
        new_node = Node(node.val)
        self.visited[node] = new_node

        # Run through the neighbors, and call cloneGraph for each neighbor
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neighbor))
        
        # return the new_node 
        return new_node


        


        




        