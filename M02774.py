n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
if(sum(a)<k):
    print(0)
else:
    ans=0
    l=1
    r=max(a)
    while(l<=r):
        mid=(l+r)>>1
        cnt=0
        for i in a:
            cnt+=i//mid
        if(cnt>=k):
            ans=max(ans,mid)
            l=mid+1
        else:
            r=mid-1
    print(ans)