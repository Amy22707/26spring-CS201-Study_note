# Definition for a binary tree node.
from typing import Optional
from math import inf
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre=-inf
        def search(node):
            nonlocal pre
            if(node is None):
                return True
            if(not search(node.left)):
                return False
            if(node.val<=pre):
                return False
            pre=node.val
            return search(node.right)
        return search(root)