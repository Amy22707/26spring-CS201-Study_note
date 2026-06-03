import sys
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
tree=[[] for _ in range(n+1)]
vis=[0]*(n+1)
ans=0
def dfs(x,k,stat):
    global ans
    if(k>m):
        return
    flag=0
    for i in tree[x]:
        if(not vis[i]):
            flag=1
            vis[i]=1
            if(a[i]==1 and stat==1):
                dfs(i,k+1,1)
            elif(a[i]==1 and stat==0):
                dfs(i,1,1)
            else:
                dfs(i,0,0)
    if(flag==0):
        ans+=1
        return

for i in range(n-1):
    u,v=map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)
vis[1]=1
if(a[1]==1):
    dfs(1,1,1)
else:
    dfs(1,0,0)
print(ans)