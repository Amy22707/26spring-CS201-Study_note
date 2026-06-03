class NumArray:

    def __init__(self, nums: list[int]):
        n=len(nums)
        sum=[0]*(n+1)
        for i in range(n):
            sum[i+1]=sum[i]+nums[i]
        self.sum=sum
    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right+1]-self.sum[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
obj=NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))