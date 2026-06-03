n,m=map(int,input().split())
goods=[[-1 for _ in range(m)]for _ in range(n)]
shops=[[]for _ in range(m)]
for i in range(n):
    s=list(input().split())
    for c in s:
        x,y=map(int,c.split(':'))
        goods[i][x-1]=y
for i in range(m):
    s=list(input().split())
    for c in s:
        x,y=map(int,c.split("-"))
        shops[i].append((x,y))
for i in range(m):
    shops[i]=sorted(shops[i],key=lambda x:-x[1])
shop_sum=[0]*m
vis=[[0 for _ in range(m)]for _ in range(n)]
ans=float("inf")
def op(sum):
    for i in range(m):
        for x,y in shops[i]:
            if(shop_sum[i]>=x):
                sum-=y
                break
    return sum
def dfs(sum,cur):
    global ans,shop_sum
    if(cur==n):
        sum-=(sum//300)*50
        ans=min(ans,op(sum))
        return
    for i in range(m):
        if(goods[cur][i]!=-1 and vis[cur][i]==0):
            sum+=goods[cur][i]
            shop_sum[i]+=goods[cur][i]
            vis[cur][i]=1
            dfs(sum,cur+1)
            shop_sum[i]-=goods[cur][i]
            vis[cur][i]=0
            sum-=goods[cur][i]
dfs(0,0)
print(ans)