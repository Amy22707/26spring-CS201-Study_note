class SegmentTree:
    def __init__(self,n,nums):
        self.n=n
        self.nums=nums
        self.tree=[0]*(n*4)
        self.lazy=[0]*(n*4)
        self.build(1,1,n)
    def pushup(self,node):
        self.tree[node]=max(self.tree[node*2],self.tree[node*2+1])
    def pushdown(self,node,l,r):
        if(self.lazy[node]!=0):
            mid=(l+r)>>1
            self.tree[node*2]+=self.lazy[node]
            self.tree[node*2+1]+=self.lazy[node]
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
            self.tree[node]+=val
            self.lazy[node]+=val
            return
        if(end<l or start>r):
            return
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        self.update_range(node*2,start,mid,l,r,val)
        self.update_range(node*2+1,mid+1,end,l,r,val)
        self.pushup(node)
    def query(self,node,start,end,l,r):
        if(l<=start and end<=r):
            return self.tree[node]
        if(end<l or start>r):
            return 0
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        return max(self.query(node*2,start,mid,l,r),self.query(node*2+1,mid+1,end,l,r))
n,q=map(int,input().split())
tree=SegmentTree(n,[0]*(n+1))
for _ in range(q):
    s=input().split()
    op=s[0]
    if(op=='Add'):
        l,r,v=map(int,s[1:])
        tree.update_range(1,1,n,l,r,v)
    elif(op=="Query"):
        l,r=map(int,s[1:])
        print(tree.query(1,1,n,l,r))