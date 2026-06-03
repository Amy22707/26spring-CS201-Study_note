n=int(input())
g=[[]for _ in range(n)]
for i in range(n-1):
    u,v=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
a=set(list(map(int,input().split())))
vis=[0]*n
def dfs(x):
    for i in g[x]:
        if(vis[i]==0 and i not in a):
            vis[i]=1
            dfs(i)
vis[0]=1
dfs(0)
print(sum(vis))