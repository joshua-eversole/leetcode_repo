class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        # Given the node, add each ancestor to a set
        def findPath(node):
            path = set()
            while node:
                path.add(node) 
                node = node.parent
            return path

        # Get the paths for p and q
        p_path = findPath(p)
        q_path = findPath(q)

        # Look through node p to find if it's in p-path
        while q:
            if q in p_path: 
                return q  
            q = q.parent
