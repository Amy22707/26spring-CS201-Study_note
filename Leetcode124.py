# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxm=-float('inf')
        def maxgain(node):#以node为根,相当于node的贡献
            nonlocal maxm
            if(node is None):
                return 0
            left_gain=max(maxgain(node.left),0)
            right_gain=max(maxgain(node.right),0)
            maxm=max(maxm,node.val+left_gain+right_gain)
            return node.val+max(left_gain,right_gain)
        maxgain(root)
        return maxm