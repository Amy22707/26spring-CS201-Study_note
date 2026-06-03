from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def op(l,r):
            if(l>r):
                return None
            mid=(l+r)>>1
            root=TreeNode(nums[mid])
            root.left=op(l,mid-1)
            root.right=op(mid+1,r)
            return root
        return op(0,len(nums)-1)
print(Solution().sortedArrayToBST([-10,-3,0,5,9]))