class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans=0
        mod=1000000007
        for i in range(1,n+1):
            t=i.bit_length()
            ans=(ans<<t)|i
            ans%=mod
        return ans
print(Solution().concatenatedBinary(3))