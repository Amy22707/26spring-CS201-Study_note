import heapq
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    a=[]
    for i in range(m):
        t=list(map(int,input().split()))
        a.append(sorted(t))
    ans=a[0].copy()
    for k in range(1,m):
        minq=[]
        cur=[]
        for i in range(n):
            heapq.heappush(minq,(ans[i]+a[k][0],i,0))
        for i in range(n):
            sum,idx1,idx2=heapq.heappop(minq)
            cur.append(sum)
            if(idx2+1<n):
                heapq.heappush(minq,(ans[idx1]+a[k][idx2+1],idx1,idx2+1))
        ans=cur.copy()
    print(*ans)
        