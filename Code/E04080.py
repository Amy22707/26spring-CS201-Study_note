import heapq
n=int(input())
a=list(map(int,input().split()))
q=[]
for i in a:
    heapq.heappush(q,i)
ans=0
while(len(q)>1):
    x=heapq.heappop(q)
    y=heapq.heappop(q)
    ans+=x+y
    heapq.heappush(q,x+y)
print(ans)