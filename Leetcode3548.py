class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        sum=0
        for i in range(m):
            for j in range(n):
                sum+=grid[i][j]
        def check(a):
            m=len(a)
            n=len(a[0])
            st=set()
            st.add(0)
            s=0
            for i in range(m-1):
                for j in range(n):
                    x=a[i][j]
                    s+=x
                    if(i>0 or j==0 or j==n-1):
                        st.add(x)
                if(n==1):
                    if(s*2==sum or s*2==sum+a[0][0] or s*2==sum+a[i][0]):
                        return True
                    continue
                if(s*2-sum in st):
                    return True
                if(i==0):
                    st.update(a[i])
            return False
        return (check(grid) or check(grid[::-1]) or check(list(zip(*grid))) or check(list(zip(*grid))[::-1]))
print(Solution().canPartitionGrid([[1,4],[2,3]]))