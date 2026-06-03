class NumArray:

    def __init__(self, nums: list[int]):
        n=len(nums)
        self.num=nums
        self.tree=[0]*(n+1)
        for i in range(n):
            self.add(i+1,nums[i])
    def lowbit(x):
        return x&(-x)
    def add(self,idx,val):
        while(idx<len(self.tree)):
            self.tree[idx]+=val
            idx+=NumArray.lowbit(idx)
    def prefix(self,index):
        ans=0
        while(index>0):
            ans+=self.tree[index]
            index-=NumArray.lowbit(index)
        return ans
    def update(self, index: int, val: int) -> None:
        self.add(index+1,val-self.num[index])
        self.num[index]=val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix(right+1)-self.prefix(left)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
obj=NumArray([1,3,5])
print(obj.sumRange(0,2))
obj.update(1,2)
print(obj.sumRange(0,2))