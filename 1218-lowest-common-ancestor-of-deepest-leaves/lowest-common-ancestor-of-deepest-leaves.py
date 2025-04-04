# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def goDeeper(node, depth):
            # Base case: if node is None, return None and the current level
            if not node:
                return (None, depth)
            
            left_lca, left_depth = goDeeper(node.left, depth + 1)
            right_lca, right_depth = goDeeper(node.right, depth + 1)

            # If left subtree is deeper, go to its LCA
            if left_depth > right_depth:
                return (left_lca, left_depth)
            # If right subtree is deeper, do the opposite
            elif right_depth > left_depth:
                return (right_lca, right_depth)
            # If they're the same, return the node and either depth
            else:
                return (node, left_depth)

        result, depth = goDeeper(root, 0)
        return result
