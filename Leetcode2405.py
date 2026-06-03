class Solution:
    def partitionString(self, s: str) -> int:
        ans=0
        a=set()
        n=len(s)
        for i in range(n):
            if(s[i] in a):
                ans+=1
                a=set()
            a.add(s[i])
        if(len(a)!=0):
            ans+=1
        return ans
print(Solution().partitionString("abacaba"))