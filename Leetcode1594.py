class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp_max=[[-1 for _ in range(n)]for _ in range(m)]
        dp_min=[[-1 for _ in range(n)]for _ in range(m)]
        dp_max[0][0]=grid[0][0]
        dp_min[0][0]=grid[0][0]
        for i in range(1,m):
            dp_min[i][0]=dp_min[i-1][0]*grid[i][0]
            dp_max[i][0]=dp_max[i-1][0]*grid[i][0]
        for i in range(1,n):
            dp_min[0][i]=dp_min[0][i-1]*grid[0][i]
            dp_max[0][i]=dp_max[0][i-1]*grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                dp_min[i][j]=min(dp_min[i-1][j]*grid[i][j],dp_max[i-1][j]*grid[i][j],dp_min[i][j-1]*grid[i][j],dp_max[i][j-1]*grid[i][j])
                dp_max[i][j]=max(dp_min[i-1][j]*grid[i][j],dp_max[i-1][j]*grid[i][j],dp_min[i][j-1]*grid[i][j],dp_max[i][j-1]*grid[i][j])
        t=dp_max[m-1][n-1]
        mod=10**9+7
        if(t<0):
            return -1
        else:
            return t%mod
print(Solution().maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))