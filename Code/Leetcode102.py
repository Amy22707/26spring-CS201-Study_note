from typing import Optional,List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        res=[]
        if(root):
            q.append(root)
        while(q):
            n=len(q)
            ans=[]
            for i in range(n):
                node=q.popleft()
                if(node is None):
                    continue
                ans.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            res.append(ans)
        return res

print(Solution().levelOrder(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))
