from math import log2
n,t=map(int,input().split())
tree=[[] for _ in range(n+1)]
for i in range(n-1):
    x,y=map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)
p,q,v1,v2=map(int,input().split())
max_log=20
par=[0]*(n+1)
dep=[0]*(n+1)
def dfs(node,parent,depth):
    par[node]=parent
    dep[node]=depth
    for i in tree[node]:
        if(i!=parent):
            dfs(i,node,depth+1)
    return
dfs(t,0,0)
up=[[0 for _ in range(max_log)]for _ in range(n+1)]
for i in range(1,n+1):
    up[i][0]=par[i]
for j in range(1,max_log):
    for i in range(1,n+1):
        up[i][j]=up[up[i][j-1]][j-1]
def lca(x,y):
    if(dep[x]<dep[y]):
        x,y=y,x
    diff=dep[x]-dep[y]
    for i in range(max_log):
        if((diff>>i)&1):
            x=up[x][i]
    if(x==y):
        return x
    for i in range(max_log-1,-1,-1):
        if(up[x][i]!=up[y][i]):
            x=up[x][i]
            y=up[y][i]
    return par[x]
def get(x,k):
    for i in range(max_log):
        if((k>>i)&1):
            x=up[x][i]
    return x
lca_node=lca(p,q)
d1=dep[p]-dep[lca_node]
d2=dep[q]-dep[lca_node]
tot=(d1+d2)//(v1+v2)
s1=tot*v1
ans=0
if(s1<=d1):
    ans=get(p,s1)
else:
    ans=get(q,d1+d2-s1)
print(tot,dep[ans])