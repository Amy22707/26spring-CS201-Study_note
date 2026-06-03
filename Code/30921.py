n,q,s=map(int,input().split())
fa=[i for i in range(n+1)]
siz=[1]*(n+1)
group=[set([i]) for i in range(n+1)]
ans=n
def find(x):
    if(fa[x]==x):
        return x
    fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    global ans
    fx=find(x)
    fy=find(y)
    if(fx==fy):
        return
    if(siz[fx]<siz[fy]):
        fx,fy=fy,fx
    fa[fy]=fx
    siz[fx]+=siz[fy]
    group[fx]|=group[fy]
    ans-=1
for i in range(q):
    x,y=map(int,input().split())
    merge(x,y)
    fx=find(x)
    if(siz[fx]>=s):
        ans+=siz[fx]-1
        for j in group[fx]:
            if(j==fx):
                continue
            fa[j]=j
            siz[j]=1
            group[j]=set([j])
        fa[fx]=fx
        siz[fx]=1
        group[fx]=set([fx])
    print(ans)
    # for j in range(1,n+1):
    #     print(find(j),end=" ")