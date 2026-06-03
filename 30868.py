import heapq
a,b,c=map(int,input().split())
query=int(input())
step=[]
if(a>0):
    step.append(a)
if(b>0):
    step.append(b)
if(c>0):
    step.append(c)
step.sort()
if(len(step)>=2):
    m=step[0]
    edges=step[1:]
    dist=[float("inf")]*m
    dist[0]=0
    q=[]
    heapq.heappush(q,(0,0))
    while(q):
        d,node=heapq.heappop(q)
        if(d>dist[node]):
            continue
        for i in edges:
            nxt=(node+i)%m
            if(dist[nxt]>d+i):
                dist[nxt]=d+i
                heapq.heappush(q,(dist[nxt],nxt))
def solve(h):
    if(len(step)==0):
        if(h==0):
            return True
        else:
            return False
    elif(len(step)==1):
        if(h%step[0]==0):
            return True
        else:
            return False
    rem=h%m
    if(dist[rem]<=h):
        return True
    else:
        return False
for i in range(query):
    h=int(input())
    if(solve(h)):
        print("Yes")
    else:
        print("No")