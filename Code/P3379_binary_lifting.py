from math import log2
import sys
sys.setrecursionlimit(10**7)
def dfs(parent,node,depth):
    p[node]=parent
    dep[node]=depth
    for i in tree[node]:
        if(i!=parent):
            dfs(node,i,depth+1)
n,m,root=map(int,input().split())
tree=[[] for _ in range(n+1)]
for i in range(n-1):
    x,y=map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)
max_log=20
up=[[0 for _ in range(max_log)]for _ in range(n+1)]#i的2^j祖先
dep=[0]*(n+1)
p=[0]*(n+1)
dfs(0,root,0)
for i in range(1,n+1):
    up[i][0]=p[i]
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
    return p[x]
for _ in range(m):
    x,y=map(int,input().split())
    print(lca(x,y))