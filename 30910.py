import heapq
n,m=map(int,input().split())
a=[[]for _ in range(n+1)]
b=[[]for _ in range(n+1)]
for i in range(m):
    x,y,z=map(int,input().split())
    a[x].append((y,z))
    b[y].append((x,z))
dist=[float("inf") for _ in range(n+1)]
dist[1]=0
dist2=[float("inf") for _ in range(n+1)]
dist2[1]=0
h=[]
heapq.heappush(h,(0,1))
while(h):
    d,node=heapq.heappop(h)
    if(d>dist[node]):
        continue
    for nxt,cost in a[node]:
        if(dist[node]+cost<dist[nxt]):
            dist[nxt]=dist[node]+cost
            heapq.heappush(h,(dist[nxt],nxt))
h=[]
heapq.heappush(h,(0,1))
while(h):
    d,node=heapq.heappop(h)
    if(d>dist2[node]):
        continue
    for nxt,cost in b[node]:
        if(dist2[node]+cost<dist2[nxt]):
            dist2[nxt]=dist2[node]+cost
            heapq.heappush(h,(dist2[nxt],nxt))
ans=0
for i in range(1,n+1):
    ans+=dist[i]+dist2[i]
print(ans)
