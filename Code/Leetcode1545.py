class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans="0"
        for i in range(n-1):
            t=ans[::-1]
            qaq=""
            for j in range(len(t)):
                qaq+=str(int(t[j])^1)
            ans=ans+"1"+qaq
        return ans[k-1]
print(Solution().findKthBit(3, 1))
