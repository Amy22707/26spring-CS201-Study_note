L,n,m=map(int,input().split())
a=[0]
for i in range(n):
    t=int(input())
    a.append(t)
a.append(L)
l=0
r=L
ans=0
while(l<=r):
    mid=(l+r)>>1
    cnt=0
    cur=0
    for i in range(1,n+2):
        if(a[i]-a[cur]<mid):
            cnt+=1
        else:
            cur=i
    if(cnt>m):
        r=mid-1
    else:
        ans=max(ans,mid)
        l=mid+1
print(ans)