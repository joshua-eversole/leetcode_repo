# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # first thoughts: this is definitely DFS, could be BFS too but i like the way BFSW is structured for this. just go down and keep the path, and check
        self.good_nodes = 0
        node_path = defaultdict(int)
        def dfs(node, max_num):
            # Base case: if not node
            if not node:
                return
            # check if the node is good
            if node.val >= max_num:
                self.good_nodes += 1
                max_num = node.val
            
            dfs(node.left, max_num)
            dfs(node.right, max_num)
        
        dfs(root, root.val - 1)
        return self.good_nodes


            
        
            
            