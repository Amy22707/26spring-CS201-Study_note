class Solution:
    def reverseBits(self, n: int) -> int:
        ans=0
        for i in range(32):
            if(n==0):
                break
            ans|=((n&1)<<(31-i))
            n=n>>1
        return ans
print(Solution().reverseBits(43261596))