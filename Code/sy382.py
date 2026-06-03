n,m=map(int,input().split())
a=[[] for _ in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    a[u].append(v)
vis=[0]*n
flag=0
def dfs(node):
    global flag
    for c in a[node]:
        if(vis[c]==0):
            vis[c]=2
            dfs(c)
        elif(vis[c]==2):
            flag=1
            return
        vis[c]=1
for i in range(n):
    if(vis[i]==0):
        vis[i]=2
        dfs(i)
        vis[i]=1
    if(flag==1):
        break
if(flag==1):
    print("Yes")
else:
    print("No")
