from collections import deque
import sys
n,p=map(int,input().split())
a=[0]
b=[0]
for i in range(n):
    u,v=map(int,input().split())
    a.append(u)
    b.append(v)
g=[[]for _ in range(n+1)]
in_deg=[0]*(n+1)
out_deg=[0]*(n+1)
for i in range(p):
    u,v,w=map(int,input().split())
    g[u].append((v,w))
    in_deg[v]+=1
    out_deg[u]+=1
    if(v==u):
        print("NULL")
        sys.exit(0)
q=deque()
cnt=0
for i in range(1,n+1):
    if(in_deg[i]==0):
        q.append(i)
        cnt+=1
while(q):
    idx=q.popleft()
    if(a[idx]<=0):
        a[idx]=0
    for i,w in g[idx]:
        a[i]+=w*a[idx]
        in_deg[i]-=1
        if(in_deg[i]==0):
            cnt+=1
            a[i]-=b[i]
            q.append(i)
flag=0
if(cnt<n):
    print("NULL")
else:
    for i in range(1,n+1):
        if(out_deg[i]==0 and a[i]>0):
            flag=1
            print(i,a[i])
    if(flag==0):
        print("NULL")