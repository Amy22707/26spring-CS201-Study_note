class NumArray:
    def __init__(self, nums: list[int]):
        self.n=len(nums)
        self.nums=nums
        self.tree=[0]*(self.n*4)
        self.lazy=[0]*(self.n*4)
        self.build(1,0,self.n-1)

    def pushup(self,node):
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]
    def pushdown(self,node,l,r):
        if(self.lazy[node]!=0):
            mid=(l+r)>>1
            self.tree[node*2]+=(mid-l+1)*self.lazy[node]
            self.tree[node*2+1]+=(r-mid)*self.lazy[node]
            self.lazy[node*2]+=self.lazy[node]
            self.lazy[node*2+1]+=self.lazy[node]
            self.lazy[node]=0    
    def build(self,node,l,r):
        if(l==r):
            self.tree[node]=self.nums[l]
            return
        mid=(l+r)>>1
        self.build(node*2,l,mid)
        self.build(node*2+1,mid+1,r)
        self.pushup(node)

    def update_range(self,node,start,end,l,r,val):
        if(l<=start and end<=r):
            self.tree[node]+=(end-start+1)*val
            self.lazy[node]+=val
            return
        if(end<l or start>r):
            return
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        self.update_range(node*2,start,mid,l,r,val)
        self.update_range(node*2+1,mid+1,end,l,r,val)
        self.pushup(node)

    def sums(self,node,start,end,l,r):#l-r目标区间，start-end当前区间
        if(l<=start and end<=r):
            return self.tree[node]
        if(end<l or start>r):
            return 0
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        return self.sums(node*2,start,mid,l,r)+self.sums(node*2+1,mid+1,end,l,r)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.sums(1,0,self.n-1,left,right)