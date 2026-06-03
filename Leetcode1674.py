from typing import List
from math import inf
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n=len(nums)
        diff=[0]*(limit*2+2)#diff[i]:全部变成i的操作数的差分
        for i in range(n//2):
            x=nums[i]
            y=nums[n-1-i]
            l=min(x,y)+1
            r=max(x,y)+limit
            #[2.l-1]+=2
            diff[2]+=2
            diff[l]-=2
            #[l,r]+=1
            diff[l]+=1
            diff[r+1]-=1
            #去除x+y
            diff[x+y]-=1
            diff[x+y+1]+=1
            #[r+1,limit*2]+2
            diff[r+1]+=2
        ans=inf
        sum=0
        for i in range(2,limit*2+1):
            sum+=diff[i]
            ans=min(ans,sum)
        return ans