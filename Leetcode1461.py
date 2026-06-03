class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=len(s)
        st=set()
        if(k>n):
            return False
        num=int(s[:k],2)
        st.add(num)
        for i in range(k,n):
            num=(num-(int(s[i-k])<<(k-1)))*2+int(s[i])
            st.add(num)
        return len(st)==(1<<k)
print(Solution().hasAllCodes("00110110", 2))