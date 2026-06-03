from collections import deque
n,m=map(int,input().split())
a=[0]+list(map(int,input().split()))
g=[[]for _ in range(n+1)]
in_deg=[0]*(n+1)
for i in range(m):
    u,v=map(int,input().split())
    g[u].append(v)
    in_deg[v]+=1
q=deque()
ve=[0]*(n+1)
cnt=0
for i in range(1,n+1):
    if(in_deg[i]==0):
        q.append(i)
        cnt+=1
while(q):
    idx=q.popleft()
    for i in g[idx]:
        ve[i]=max(ve[i],ve[idx]+a[idx])
        in_deg[i]-=1
        if(in_deg[i]==0):
            q.append(i)
            cnt+=1
if(cnt!=n):
    print(-1)
else:
    ans=0
    for i in range(1,n+1):
        ans=max(ans,ve[i]+a[i])
    print(ans)