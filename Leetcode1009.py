class Solution:
    def bitwiseComplement(self, n: int) -> int:
        t=n.bit_length()
        return n^((1<<t)-1) if n>0 else 1
print(Solution().bitwiseComplement(5))