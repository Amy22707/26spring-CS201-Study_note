from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        s=[]
        node=root
        while(node is not None or len(s)>0):
            while(node is not None):
                s.append(node)
                node=node.left
            node=s.pop()
            res.append(node.val)
            node=node.right
        return res

print(Solution().inorderTraversal(TreeNode(1,None,TreeNode(2,TreeNode(3)))))