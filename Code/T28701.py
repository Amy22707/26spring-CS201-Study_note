n,k=map(int,input().split())
t=list(map(int,input().split()))
t.sort(reverse=True)
s=sum(t)
idx=0
while(idx<n and t[idx]>s/k):
    s-=t[idx]
    k-=1
    idx+=1
print(f"{s/k:.3f}")