from collections import deque
import sys
sys.setrecursionlimit(1000000)
n,m=map(int,input().split())
p=[0]+list(map(int,input().split()))
a=[[]for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    a[x].append(y)
dfn=[0]*(n+1)
low=[0]*(n+1)
time=0
s=[]
scc=[]
idx=[0]*(n+1)
val=[]
def tarjan(k):
    global time
    time+=1
    low[k]=dfn[k]=time
    s.append(k)
    for i in a[k]:
        if(dfn[i]==0):
            tarjan(i)
            low[k]=min(low[k],low[i])
        elif(i in s):
            low[k]=min(low[k],dfn[i])
    if(low[k]==dfn[k]):
        tmp=[]
        sum=0
        while(True):
            x=s.pop()
            tmp.append(x)
            sum+=p[x]
            idx[x]=len(scc)
            if(x==k):
                break
        scc.append(tmp)
        val.append(sum)
for i in range(1,n+1):
    if(dfn[i]==0):
        tarjan(i)
lens=len(scc)
in_deg=[0]*lens
dag=[[]for _ in range(lens)]
for i in range(1,n+1):
    for j in a[i]:
        if(idx[i]!=idx[j]):
            in_deg[idx[j]]+=1
            dag[idx[i]].append(idx[j])
q=deque()
dp=[0]*lens
for i in range(lens):
    if(in_deg[i]==0):
        q.append(i)
        dp[i]=val[i]
while(q):
    x=q.popleft()
    for i in dag[x]:
        dp[i]=max(dp[i],dp[x]+val[i])
        in_deg[i]-=1
        if(in_deg[i]==0):
            q.append(i)
print(max(dp))