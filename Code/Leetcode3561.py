class Solution:
    def resultingString(self, s: str) -> str:
        stk=[]
        for c in s:
            if(stk and (abs(ord(stk[-1])-ord(c))==1 or abs(ord(stk[-1])-ord(c))==25)):
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)

print(Solution().resultingString("abc"))