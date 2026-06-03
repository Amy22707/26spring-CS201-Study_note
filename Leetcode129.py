# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,sum):
            if(node==None):
                return 0
            sum=sum*10+node.val
            if(node.left==None and node.right==None):
                return sum
            return dfs(node.left,sum)+dfs(node.right,sum)
        return dfs(root,0)
print(Solution().sumNumbers(TreeNode(1,TreeNode(2),TreeNode(3))))