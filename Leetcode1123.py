from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if(node is None):
                return (None,0)
            lca_left,depth_left=dfs(node.left)
            lca_right,depth_right=dfs(node.right)
            if(depth_left==depth_right):
                return (node,depth_left+1)
            elif(depth_left>depth_right):
                return (lca_left,depth_left+1)
            elif(depth_left<depth_right):
                return (lca_right,depth_right+1)
        return dfs(root)[0]
print(Solution().lcaDeepestLeaves(TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))))
        