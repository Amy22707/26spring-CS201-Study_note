class NumArray:
    def __init__(self, nums: list[int]):
        self.n=len(nums)
        self.nums=nums
        self.tree=[0]*(self.n*4)
        self.build(1,0,self.n-1)
        
    def build(self,node,l,r):
        if(l==r):
            self.tree[node]=self.nums[l]
            return
        mid=(l+r)>>1
        self.build(node*2,l,mid)
        self.build(node*2+1,mid+1,r)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]

    def update_tree(self,node,l,r,idx,val):
        if(l==r):
            self.tree[node]=val
            self.nums[idx]=val
            return
        mid=(l+r)>>1
        if(idx<=mid):
            self.update_tree(node*2,l,mid,idx,val)
        else:
            self.update_tree(node*2+1,mid+1,r,idx,val)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1] 

    def update(self, index: int, val: int) -> None:
        self.update_tree(1,0,self.n-1,index,val)

    def sums(self,node,start,end,l,r):#l-r目标区间，start-end当前区间
        if(l<=start and end<=r):
            return self.tree[node]
        if(end<l or start>r):
            return 0
        mid=(start+end)>>1
        return self.sums(node*2,start,mid,l,r)+self.sums(node*2+1,mid+1,end,l,r)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.sums(1,0,self.n-1,left,right)