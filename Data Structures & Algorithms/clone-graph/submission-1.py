"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}
        def cloneNode(node):
            if node == None:
                return None

            if node in cloneMap:
                return cloneMap[node]

            cloneMap[node] = Node(node.val, [])
            clone = cloneMap[node]

            for neighbor in node.neighbors:
                clone.neighbors.append(cloneNode(neighbor))

            return clone


        return cloneNode(node)