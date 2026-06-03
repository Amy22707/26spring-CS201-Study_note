from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        def get(a):
            n=len(a)
            dp=[0]*n
            dp[0]=a[0]
            if(n==1):
                return dp[0]
            dp[1]=max(a[0],a[1])
            for i in range(2,n):
                dp[i]=max(dp[i-1],dp[i-2]+a[i])
            return dp[n-1]
        return max(get(nums[:-1]), get(nums[1:]))

print(Solution().rob([2,3,2]))