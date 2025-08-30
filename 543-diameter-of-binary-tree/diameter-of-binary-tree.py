# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # For each level, return the max of the left side and the right side
        self.result = 0
        def dfs(node):
            # Base case: if it doesn't exist, don't return anything positive
            if not node:
                return 0
            # Recursive case: compare the result to the current left+right
            left = dfs(node.left)
            right = dfs(node.right)
            self.result = max(self.result, left + right)

            return max(left, right) + 1
        
        dummy = dfs(root)
        return self.result


            
