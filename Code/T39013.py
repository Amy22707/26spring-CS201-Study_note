import sys
from math import sqrt,ceil
from collections import deque
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
g=[[]for _ in range(n+1)]
for i in range(m):
    x,y,w=map(int,input().split())
    g[x].append((y,w))
start=int(input())
dfn=[0]*(n+1)
low=[0]*(n+1)
time=0
s=[]
scc=[]
in_s=[0]*(n+1)
idx=[0]*(n+1)
def tarjan(k):
    global time
    time+=1
    low[k]=dfn[k]=time
    s.append(k)
    in_s[k]=1
    for i,qaq in g[k]:
        if(dfn[i]==0):
            tarjan(i)
            low[k]=min(low[k],low[i])
        elif(in_s[i]):
            low[k]=min(low[k],dfn[i])
    if(low[k]==dfn[k]):
        tmp=[]
        while(True):
            x=s.pop()
            tmp.append(x)
            idx[x]=len(scc)
            in_s[x]=0
            if(x==k):
                break
        scc.append(tmp)
for i in range(1,n+1):
    if(dfn[i]==0):
        tarjan(i)
lens=len(scc)
in_deg=[0]*lens
vis=set()
dag=[[]for _ in range(lens)]
sums=[[] for _ in range(lens)]
for i in range(1,n+1):
    for j,qaq in g[i]:
        if(idx[i]!=idx[j]):
            in_deg[idx[j]]+=1
            dag[idx[i]].append((idx[j],qaq))
        else:
            sums[idx[i]].append(qaq)
res=[]
for i in range(lens):
    cnt=0
    for j in sums[i]:
        k=ceil((sqrt(8*j+1)-1)/2)
        val=k*j-(k-1)*k*(k+1)//6
        cnt+=val
    res.append(cnt)
q=deque()
dp=[-1]*lens
sidx=idx[start]
dp[sidx]=res[sidx]
for i in range(lens):
    if(in_deg[i]==0):
        q.append(i)
while(q):
    node=q.popleft()
    for i,val in dag[node]:
        if(dp[node]!=-1):
            dp[i]=max(dp[i],dp[node]+res[i]+val)
        in_deg[i]-=1
        if(in_deg[i]==0):
            q.append(i)
print(int(max(dp)))