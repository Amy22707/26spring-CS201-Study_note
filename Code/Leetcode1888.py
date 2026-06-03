class Solution:
    def minFlips(self, s: str) -> int:
        target="01"
        n=len(s)
        cnt=0
        for i in range(n):
            if(s[i]!=target[i%2]):
                cnt+=1
        ans=min(cnt,n-cnt)
        s+=s
        for i in range(1,n):
            if(s[i-1]!=target[(i-1)%2]):
                cnt-=1
            if(s[i+n-1]!=target[(i+n-1)%2]):
                cnt+=1
            ans=min(ans,cnt,n-cnt)
        return ans
print(Solution().minFlips("111000"))