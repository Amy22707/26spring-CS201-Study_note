class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        a=[[0 for _ in range(n+1)]for _ in range(m+1)]
        check=[[0 for _ in range(n+1)]for _ in range(m+1)]
        def trans(x):
            if(x=="X"):
                return 1
            elif(x=="Y"):
                return -1
            return 0
        for i in range(m):
            for j in range(n):
                a[i+1][j+1]=a[i][j+1]+a[i+1][j]+trans(grid[i][j])-a[i][j]
                check[i+1][j+1]=check[i][j+1]|check[i+1][j]|abs(trans(grid[i][j]))
        ans=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(check[i][j] and a[i][j]==0):
                    ans+=1
        return ans
print(Solution().numberOfSubmatrices([["X","Y","."],["Y",".","."]]))