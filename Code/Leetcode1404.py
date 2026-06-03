class Solution:
    def numSteps(self, s: str) -> int:
        n=len(s)
        idx=s[::-1].find('1')
        if(idx==n-1):
            return n-1
        idx=n-1-idx
        ans=n+1
        for i in range(0,idx):
            if(s[i]=='0'):
                ans+=1
        return ans
print(Solution().numSteps("1101"))