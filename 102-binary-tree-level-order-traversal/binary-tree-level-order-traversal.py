# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # First thoughts: this can be done either bfs or dfs, but bfs is probably the better move

        result = []
        # Base case: if there's no root
        if not root:
            return []

        def bfs():
            q = deque()
            
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

        def dfs(node, level):
            if not node:
                return

            if len(result) < (level + 1):
                result.append([node.val])
            else:
                result[level].append(node.val)
            
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            return




        #return bfs()
        dfs(root, 0)
        return result
                

        