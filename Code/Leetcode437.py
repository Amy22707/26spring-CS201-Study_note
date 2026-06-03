# Definition for a binary tree node.
from typing import Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt=defaultdict(int)
        cnt[0]=1
        ans=0
        def dfs(node,cur_sum):
            nonlocal ans
            if(not node):
                return
            cur_sum+=node.val
            ans+=cnt[cur_sum-targetSum]
            cnt[cur_sum]+=1
            dfs(node.left,cur_sum)
            dfs(node.right,cur_sum)
            cnt[cur_sum]-=1
        dfs(root,0)
        return ans