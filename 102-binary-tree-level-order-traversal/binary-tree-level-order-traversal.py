# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # First thoughts: this can be done either bfs or dfs, but bfs is probably the better move
        q = deque()
        result = []
        # Base case: if there's no root
        if not root:
            return []
        
        q.append(root)

        while q:
            row = []
            # Inner while q is to get everything in the existing row out 
            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                row.append(node.val)
            result.append(row)
        
        return result
                

        