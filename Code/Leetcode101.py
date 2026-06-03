# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check(p,q):
        if(p is None and q is None):
            return True
        if(p is None or q is None):
            return False
        if(p.val!=q.val):
            return False
        return Solution.check(p.left,q.right) and Solution.check(p.right,q.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return True
        return Solution.check(root.left,root.right)