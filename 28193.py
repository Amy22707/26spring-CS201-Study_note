n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
g=[[]for _ in range(n+1)]
vis=[0]*(n+1)
minm=[0]
for i in range(m):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
def dfs(x,tag):
    for i in g[x]:
        if(vis[i]==0):
            vis[i]=tag
            minm[tag]=min(minm[tag],a[i])
            dfs(i,tag)
cnt=1
for i in range(1,n+1):
    if(vis[i]==0):
        vis[i]=cnt
        minm.append(a[i])
        dfs(i,cnt)
        cnt+=1
ans=sum(minm)
print(ans)
