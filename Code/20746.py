from math import ceil
a=list(map(int,input().split(",")))
t=int(input())
l=1
r=max(a)
ans=r
while(l<=r):
    mid=(l+r)>>1
    s=0
    for i in a:
        s+=ceil(i/mid)
    if(s<=t):
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)