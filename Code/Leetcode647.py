class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(2*n-1):
            l=i//2
            r=(i+1)//2
            while(l>=0 and r<n and s[l]==s[r]):
                l-=1
                r+=1
                ans+=1
        return ans
print(Solution().countSubstrings("abc"))