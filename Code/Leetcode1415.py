class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if(k>3*(1<<(n-1))):
            return ""
        ans=[]
        def dfs(cur,step):
            if(step==n):
                ans.append(cur)
                return
            if(step==0):
                dfs("a",step+1)
                dfs("b",step+1)
                dfs("c",step+1)
            else:
                if(cur[-1]!='a'):
                    dfs(cur+"a",step+1)
                if(cur[-1]!='b'):
                    dfs(cur+"b",step+1)
                if(cur[-1]!='c'):
                    dfs(cur+"c",step+1)
        dfs("",0)
        ans.sort()
        return ans[k-1]
print(Solution().getHappyString(3,9))