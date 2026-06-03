import heapq
from bisect import bisect_right
n,k=map(int,input().split())
a=list(map(int,input().split()))
sorted_a=sorted(a)
idxa=[]
for i in range(n):
    idxa.append((a[i],i))
sorted_idxa=sorted(idxa)
rank_to_h=[0]*(n+1)#rank->高度
pos_to_rank=[0]*(n+1)#原始下标->rank
for i in range(n):
    x,idx=sorted_idxa[i]
    pos_to_rank[idx]=i+1
    rank_to_h[i+1]=x

def lowbit(x):
    return x&(-x)
bit=[0]*(n+1)
def bit_add(idx,v):
    while(idx<=n):
        bit[idx]+=v
        idx+=lowbit(idx)
def bit_query(idx):
    res=0
    while(idx>0):
        res+=bit[idx]
        idx-=lowbit(idx)
    return res
deg=[0]*(n+1)
for i in range(n):
    cur_rank=pos_to_rank[i]
    cur_h=rank_to_h[cur_rank]
    x=bisect_right(sorted_a,cur_h-k-1)
    y=bisect_right(sorted_a,cur_h+k)
    deg[cur_rank]=bit_query(x)+(i-bit_query(y))
    bit_add(cur_rank,1)
tree=[(0,0)]*(4*n)
tag=[0]*(4*n)
def build(node,l,r):
    if(l==r):
        tree[node]=(deg[l],l)
        return
    mid=(l+r)//2
    build(node*2,l,mid)
    build(node*2+1,mid+1,r)
    tree[node]=min(tree[node*2],tree[node*2+1])
def push_up(node,val):
    tag[node]+=val
    tree[node]=(tree[node][0]+val,tree[node][1])
def push_down(node):
    if(tag[node]!=0):
        push_up(node*2,tag[node])
        push_up(node*2+1,tag[node])
        tag[node]=0
def update(node,start,end,l,r,val):
    if(start>r or end<l):
        return
    if(start>=l and end<=r):
        push_up(node,val)
        return
    push_down(node)
    mid=(start+end)//2
    update(node*2,start,mid,l,r,val)
    update(node*2+1,mid+1,end,l,r,val)
    tree[node]=min(tree[node*2],tree[node*2+1])

build(1,1,n)
res=[]
maxm=10**9
for i in range(n):
    min_deg,idx=tree[1]
    res.append(rank_to_h[idx])
    update(1,1,n,idx,idx,maxm)
    h=rank_to_h[idx]
    x=bisect_right(sorted_a,h-k-1)
    y=bisect_right(sorted_a,h+k)
    if(x>=1):
        update(1,1,n,1,x,-1)
    if(y<n):
        update(1,1,n,y+1,n,-1)
print(" ".join(map(str,res)))