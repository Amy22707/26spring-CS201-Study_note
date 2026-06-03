n=int(input())
a=[]
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)
MAXM=float("inf")
dp=[[MAXM for _ in range(1<<n)] for _ in range(n)]
dp[0][1]=0
for i in range(1,1<<n,2):
    for j in range(n):
        if(not (1<<j)&i):
            for k in range(n):
                if((1<<k)&i):
                    qaq=dp[j][i|(1<<j)]
                    qwq=dp[k][i]+a[k][j]
                    if(qwq<qaq):
                        dp[j][i|(1<<j)]=qwq
ans=MAXM
for i in range(n):
    qaq=dp[i][(1<<n)-1]+a[i][0]
    if(ans>qaq):
        ans=qaq
print(ans)