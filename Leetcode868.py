class Solution:
    def binaryGap(self, n: int) -> int:
        ans=0
        cnt=1
        flag=0
        while(n):
            if(flag==1 and n&1==0):
                cnt+=1
            elif(n&1==1):
                if(flag==0):
                    flag=1
                else:
                    ans=max(ans,cnt)
                    cnt=1
            n>>=1
        return ans
print(Solution().binaryGap(5))