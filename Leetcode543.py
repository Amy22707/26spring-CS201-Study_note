# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(root,dep):
            nonlocal ans
            if(root is None):
                return dep
            left_depth=dfs(root.left,dep+1)
            right_depth=dfs(root.right,dep+1)
            ans=max(ans,left_depth+right_depth-2*dep-2)
            return max(left_depth,right_depth)
        dfs(root,0)
        return ans