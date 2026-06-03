from collections import deque
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
maxs=[]
mins=[]
res=0
low=[0]*n
high=[0]*n
for i in range(n):
    while(maxs and a[maxs[-1]]>=a[i]):#increase
        t=maxs.pop()
        low[t]=i-1
    maxs.append(i)
while(maxs):
    t=maxs.pop()
    low[t]=n-1
a_new=a[::-1]
for i in range(n):
    while(mins and a_new[mins[-1]]<=a_new[i]):
        t=mins.pop()
        high[n-1-t]=n-i
    mins.append(i)
while(mins):
    t=mins.pop()
    high[n-1-t]=0
# print(a)
# print(low)
# print(high)
for i in range(n):
    for j in range(i+1,low[i]+1):
        if(high[j]<=i):
            res=max(res,j-i+1)
print(res)