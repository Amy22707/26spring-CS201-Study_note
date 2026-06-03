from collections import deque
n,m=map(int,input().split())
g=[[]for _ in range(n+1)]
r=[[]for _ in range(n+1)]
in_deg=[0]*(n+1)
out_deg=[0]*(n+1)
for i in range(m):
    x,y,z=map(int,input().split())
    g[x].append((y,z))
    r[y].append((x,z))
    in_deg[y]+=1
    out_deg[x]+=1
q=deque()
ve=[0]*(n+1)
for i in range(1,n+1):
    if(in_deg[i]==0):
        q.append(i)
while(q):
    node=q.popleft()
    for i,val in g[node]:
        ve[i]=max(ve[i],ve[node]+val)
        in_deg[i]-=1
        if(in_deg[i]==0):
            q.append(i)

ans=max(ve)
print(ans)
vl=[ans]*(n+1)
q=deque()
for i in range(1,n+1):
    if(out_deg[i]==0):
        q.append(i)
while(q):
    node=q.popleft()
    for i,val in r[node]:
        vl[i]=min(vl[i],vl[node]-val)
        out_deg[i]-=1
        if(out_deg[i]==0):
            q.append(i)
res=[]
for i in range(1,n+1):
    for j,k in g[i]:
        if(ve[i]+k==vl[j]):
            res.append((i,j))
res.sort()
for i,j in res:
    print(i,j)
