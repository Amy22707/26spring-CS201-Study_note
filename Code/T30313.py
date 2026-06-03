from collections import deque
n,m=map(int,input().split())
g=[[]for _ in range(n+1)]
edges=[]
for i in range(m):
    u,v,w=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
    edges.append((w,u,v))
par=[0]*(n+1)
q=deque()
un_vis=[i for i in range(1,n+1)]
marked=[0]*(n+1)
cnt=0
while(un_vis):
    cnt+=1
    start=un_vis.pop()
    q.append(start)
    par[start]=cnt
    while(q):
        idx=q.popleft()
        for i in g[idx]:
            marked[i]=1
        nxt=[]
        for i in un_vis:
            if(marked[i]==0):
                q.append(i)
                par[i]=cnt
            else:
                nxt.append(i)
        un_vis=nxt
        for i in g[idx]:
            marked[i]=0
fa=[i for i in range(cnt+1)]
def find(x):
    if(x==fa[x]):
        return x
    fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    fx=find(x)
    fy=find(y)
    if(fx==fy):
        return
    fa[fx]=fy
new_edges=[]
for w,u,v in edges:
    if(par[u]!=par[v]):
        new_edges.append((w,par[u],par[v]))
new_edges=sorted(new_edges,key=lambda x:x[0])
ans=0
tot=cnt-1
qwq=0
for w,u,v in new_edges:
    if(qwq==tot):
        break
    if(find(u)!=find(v)):
        merge(u,v)
        ans+=w
        qwq+=1
print(ans)