import sys
sys.setrecursionlimit(10**7)
n=int(input())
a=[0]
for i in range(n):
    r=int(input())
    a.append(r)
up=[[]for _ in range(n+1)]
down=[[]for _ in range(n+1)]
in_deg=[0]*(n+1)
for i in range(n-1):
    l,k=map(int,input().split())
    up[l].append(k)
    down[k].append(l)
    in_deg[l]+=1
dp1=[0]*(n+1)#i号节点参加，最大值
dp2=[0]*(n+1)#i号节点不参加，最大值
root=0
for i in range(1,n+1):
    if(in_deg[i]==0):
        root=i
        break
def dfs(x):
    dp1[x]=a[x]
    for i in down[x]:
        dfs(i)
        dp1[x]+=dp2[i]
        dp2[x]+=max(dp1[i],dp2[i])
dfs(root)
print(max(dp1[root],dp2[root]))