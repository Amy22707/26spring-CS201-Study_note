n,m=map(int,input().split())
edges=[]
for i in range(m):
    u,v,w=map(int,input().split())
    edges.append((w,u,v))
fa=[i for i in range(n+1)]
def find(x):
    if(fa[x]==x):
        return fa[x]
    fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    fx=find(x)
    fy=find(y)
    if(fx==fy):
        return
    fa[fx]=fy
cnt=0
ans=0
edges.sort(key=lambda x:x[0])
for w,u,v in edges:
    if(find(u)==find(v)):
        continue
    ans+=w
    cnt+=1
    merge(u,v)
if(cnt<n-1):
    print("orz")
else:
    print(ans)
