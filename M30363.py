n,q=map(int,input().split())
fa=[i for i in range(n+1)]
siz=[1 for i in range(n+1)]
cnt=[0 for i in range(n+1)]
from collections import defaultdict
ans=0
def find(x):
    if(x==fa[x]):
        return x
    fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    global ans
    fx=find(x)
    fy=find(y)
    if(fx==fy):
        return ans
    if(siz[fx]>siz[fy]):
        fx,fy=fy,fx
    ans-=(cnt[fx]+cnt[fy])
    fa[fx]=fy
    siz[fy]+=siz[fx]
    cnt[fx]=0
    tmp=siz[fy]
    cnt[fy]=tmp*(tmp-1)//2
    ans+=cnt[fy]
    return ans
for i in range(q):
    u,v=map(int,input().split())
    print(merge(u,v))
