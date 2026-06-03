class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n=len(grid)
        zeroes=[n]*n
        for i in range(n):
            for j in range(n-1,-1,-1):
                if(grid[i][j]==1):
                    zeroes[i]=n-1-j
                    break
        ans=0
        for i in range(n):
            qaq=n-1-i
            flag=0
            for j in range(i,n):
                if(zeroes[j]>=qaq):
                    flag=1
                    ans+=(j-i)
                    zeroes[i+1:j+1]=zeroes[i:j]
                    break
            if(flag==0):
                return -1
        return ans
print(Solution().minSwaps([[0,0,1],[1,1,0],[1,0,0]]))