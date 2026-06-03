from collections import deque
n,d=map(int,input().split())
rain=[]
for i in range(n):
    t=list(map(int,input().split()))
    rain.append(t)
rain=sorted(rain,key=lambda x:x[0])
maxq=deque()
minq=deque()
left=0
ans=float("INF")
for i in range(n):
    while(maxq and rain[maxq[-1]][1]<=rain[i][1]):
        maxq.pop()
    maxq.append(i)
    while(minq and rain[minq[-1]][1]>=rain[i][1]):
        minq.pop()
    minq.append(i)
    while(rain[maxq[0]][1]-rain[minq[0]][1]>=d and left<i):
        ans=min(ans,rain[i][0]-rain[left][0])
        if(maxq[0]==left):
            maxq.popleft()
        if(minq[0]==left):
            minq.popleft()
        left+=1
if(ans==float("INF")):
    print(-1)
else:
    print(ans)