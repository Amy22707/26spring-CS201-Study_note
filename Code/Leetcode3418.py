from typing import List
from functools import cache
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m=len(coins)
        n=len(coins[0])
        ans=float('-inf')
        @cache
        def dfs(x,y,k):
            if(x>=m or y>=n):
                return float('-inf')
            val=coins[x][y]
            if(x==m-1 and y==n-1):
                if(val<0 and k>0):
                    return 0
                return val
            res=val+max(dfs(x+1,y,k),dfs(x,y+1,k))
            if(val<0):
                if(k>0):
                    res=max(res,dfs(x+1,y,k-1),dfs(x,y+1,k-1))
            return res
        ans=dfs(0,0,2)
        dfs.cache_clear()
        return ans
print(Solution().maximumAmount([[0,1,-1],[1,-2,3],[2,-3,4]]))