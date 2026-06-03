from math import log2
import sys
sys.setrecursionlimit(10**7)
n,m,root=map(int,input().split())
tree=[[] for _ in range(n+1)]
dfn=[0]*(n+1)
dep=[0]*(n+1)
seq=[0]*(n+1)#seq[dfn[i]]
p=[0]*(n+1)
timer=0
def dfs(parent,node,depth):
    global timer
    timer+=1
    dfn[node]=timer
    seq[timer]=node
    p[node]=parent
    dep[node]=depth
    for i in tree[node]:
        if(i!=parent):
            dfs(node,i,depth+1)
for i in range(n-1):
    x,y=map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)
dep[0]=dfn[0]=float('inf')
dfs(0,root,0)
log=[0]*(n+1)
for i in range(1,n+1):
    log[i]=int(log2(i))
st=[[0 for _ in range(log[n]+1)] for _ in range(n+1)]
for i in range(1,n+1):
    st[i][0]=seq[i]
for j in range(1,log[n]+1):
    for i in range(1,n-(1<<j)+2):
        if(dep[st[i][j-1]]<dep[st[i+(1<<(j-1))][j-1]]):
            st[i][j]=st[i][j-1]
        else:
            st[i][j]=st[i+(1<<(j-1))][j-1]
def lca(x,y):
    if(x==y):
        return x
    l=dfn[x]
    r=dfn[y]
    if(l>r):
        l,r=r,l
    l+=1
    k=log[r-l+1]
    a=st[l][k]
    b=st[r-(1<<k)+1][k]
    if(dep[a]<dep[b]):
        return p[a]
    else:
        return p[b]
for _ in range(m):
    x,y=map(int,input().split())
    print(lca(x,y))