n=int(input())
a=[0]+list(map(int,input().split()))
dp1=[0 for _ in range(n+1)]#以i为根，选i
dp2=[0 for _ in range(n+1)]#以i为根，不选i
for i in range(n,0,-1):
    left=i<<1
    right=(i<<1)|1
    dp1[i]=a[i]
    if(left<=n):
        dp1[i]+=dp2[left]
        dp2[i]+=max(dp1[left],dp2[left])
    if(right<=n):
        dp1[i]+=dp2[right]
        dp2[i]+=max(dp1[right],dp2[right])
print(max(dp1[1],dp2[1]))