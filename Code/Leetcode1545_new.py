class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if(n==1):
            return '0'
        if(k==(1<<(n-1))):
            return '1'
        if(k<(1<<(n-1))):
            return self.findKthBit(n-1,k)
        res=self.findKthBit(n-1,(1<<n)-k)
        if(res=='1'):
            return '0'
        else:
            return '1'
print(Solution().findKthBit(3, 1))
