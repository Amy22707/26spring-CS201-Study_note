# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        node=root
        ans=[]
        q=deque()
        q.append(node)
        if(node==None):
            return ans
        while(q):
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if(i==n-1):
                    ans.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
        return ans