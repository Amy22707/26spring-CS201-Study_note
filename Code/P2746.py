import sys
sys.setrecursionlimit(1000000)
n=int(input())
a=[[]]
for i in range(1,n+1):
    a.append(list(map(int,input().split()))[:-1])
dfn=[0]*(n+1)
low=[0]*(n+1)
time=0
s=[]
scc=[]
idx=[0]*(n+1)
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
        while(True):
            x=s.pop()
            tmp.append(x)
            idx[x]=len(scc)
            if(x==k):
                break
        scc.append(tmp)
for i in range(1,n+1):
    if(dfn[i]==0):
        tarjan(i)
lens=len(scc)
in_deg=[0]*lens
out_deg=[0]*lens
for i in range(1,n+1):
    for j in a[i]:
        if(idx[i]!=idx[j]):
            out_deg[idx[i]]+=1
            in_deg[idx[j]]+=1
ans1=0
ans2=0
for i in range(lens):
    if(in_deg[i]==0):
        ans1+=1
    if(out_deg[i]==0):
        ans2+=1
print(ans1)
if(lens==1):
    print(0)
else:
    print(max(ans1,ans2))