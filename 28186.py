from collections import deque
n,m=map(int,input().split())
t=list(map(int,input().split()))
a=deque()
for i in range(n):
    a.append((t[i],i+1))
while(len(a)>1):
    num,idx=a.popleft()
    if(num>m):
        qaq=(num-m,idx)
        a.append(qaq)
print(a[0][1])