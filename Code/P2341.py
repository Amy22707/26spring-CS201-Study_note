import sys
sys.setrecursionlimit(1000000)
n,m=map(int,input().split())
c=[[]for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    c[x].append(y)
low=[0]*(n+1)
dfn=[0]*(n+1)
time=0
s=[]
scc=[]
idx=[0]*(n+1)
def tarjan(k):
    global time
    time+=1
    low[k]=dfn[k]=time
    s.append(k)
    for i in c[k]:
        if(dfn[i]==0):
            tarjan(i)
            low[k]=min(low[k],low[i])
        elif i in s:
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
cnt=len(scc)
out=[0]*cnt
for i in range(1,n+1):
    for j in c[i]:
        if(idx[i]!=idx[j]):
            out[idx[i]]+=1
ans=0
flag=0
for i in range(cnt):
    if(out[i]==0 and ans!=0):
        flag=1
        print(0)
        break
    elif(out[i]==0):
        ans+=len(scc[i])
if(flag==0):
    print(ans)