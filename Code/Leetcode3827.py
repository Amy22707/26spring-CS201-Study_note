class Solution:
    def countMonobit(self, n: int) -> int:
        t=n.bit_length()
        ans=t
        if(n.bit_count()==n.bit_length()):
            ans+=1
        return ans
print(Solution().countMonobit(4))