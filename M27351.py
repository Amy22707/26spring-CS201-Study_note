import sys
from collections import deque
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
g=set()
for i in range(m):
    x,y=map(int,input().split())
    g.add((x,y))
    g.add((y,x))
ans=0
vis=set()
for i in range(1,n+1):
    vis.add(i)
q=deque()
for i in range(1,n+1):
    if(i in vis):
        vis.remove(i)
        q.append(i)
        while(q):
            node=q.popleft()
            tmp=set()
            for j in vis:
                if((node,j) not in g):
                    tmp.add(j)
                    q.append(j)
            vis-=tmp           
        ans+=1
print(ans-1)