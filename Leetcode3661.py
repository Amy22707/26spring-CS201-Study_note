from cmath import inf
from typing import List
from bisect import bisect_left,bisect_right
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        a=[(0,0)]+sorted(zip(robots,distance),key=lambda x:x[0])+[(inf,0)]
        m=len(robots)
        n=len(walls)
        walls.sort()
        dp=[[0 for _ in range(2)] for _ in range(m+1)]#第i+1个机器人向左/右射击,前i个最大值
        for i in range(1,m+1):
            r=a[i][0]
            d=a[i][1]
            maxleft=max(r-d,a[i-1][0]+1)
            left=bisect_left(walls,maxleft)
            cur1=bisect_right(walls,r)
            cur2=bisect_left(walls,r)
            for j in range(2):
                if(j==0):
                    minright=min(r+d,a[i+1][0]-a[i+1][1]-1)
                else:
                    minright=min(r+d,a[i+1][0]-1)
                right=bisect_right(walls,minright)
                dp[i][j]=max(dp[i-1][0]+cur1-left,dp[i-1][1]+right-cur2)
        return max(dp[m][0],dp[m][1])

print(Solution().maxWalls([10,2],[5,1],[5,2,7]))