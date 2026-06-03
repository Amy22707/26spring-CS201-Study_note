class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        new_nums=[0]*n
        for i in range(n):
            a=nums[i-1]
            b=nums[i]
            if(i==n-1):
                c=nums[0]
            else:
                c=nums[i+1]
            new_nums[i]=max(0,max(a,c)+1-b)
        #print(new_nums)

        def get(a):
            m=len(a)
            nonlocal k
            if(k==0):
                return 0
            dp=[[float("inf") for _ in range(k+1)] for _ in range(n)]#0-i，取j个数的最小和
            dp[0][1]=a[0]
            for i in range(m):
                dp[i][0]=0
            if((m+1)//2<k):
                return -1
            if(m==1):
                return 0 if k==0 else a[0]
            dp[1][1]=min(a[0],a[1])
            for i in range(2,m):
                for j in range(1,min(i//2+2,k+1)):
                    dp[i][j]=min(dp[i-1][j],dp[i-2][j-1]+a[i])
            #print(dp)
            return dp[m-1][k]
        
        if((n+1)//2<k):
            return -1
        return min(get(new_nums[:-1]),get(new_nums[1:]))
print(Solution().minOperations([1,-4],0))