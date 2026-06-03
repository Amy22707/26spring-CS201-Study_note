import sys
sys.setrecursionlimit(10**6)
t=int(input())
def dfs(parent,x):
    if(len(a[x])==1 and a[x][0]==parent):
        ans[x]=1
    for i in a[x]:
        if(i!=parent):
            dfs(x,i)
            ans[x]+=ans[i]

for _ in range(t):
    n=int(input())
    a=[[]for _ in range(n+1)]
    ans=[0 for _ in range(n+1)]
    for i in range(n-1):
        u,v=map(int,input().split())
        a[u].append(v)
        a[v].append(u)
    q=int(input())
    dfs(0,1)
    for i in range(q):
        u,v=map(int,input().split())
        print(ans[u]*ans[v])