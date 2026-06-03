import bisect
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
maxs=[]
mins=[]
res=0
high=[0]*n
for i in range(n):
    while(maxs and a[maxs[-1]]<a[i]):#decrease
        maxs.pop()
    high[i]=maxs[-1] if maxs else -1
    maxs.append(i)
for i in range(n):
    while(mins and a[mins[-1]]>=a[i]):#increase
        mins.pop()
    t=bisect.bisect_right(mins,high[i])
    if(t<len(mins)):
        res=max(res,i-mins[t]+1)
    mins.append(i)
print(res)