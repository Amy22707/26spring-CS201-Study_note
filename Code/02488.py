t=int(input())
m,n=0,0
ans=""
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]
def dfs(x,y,res,step):
    global m,n,ans
    if(step==m*n):
        ans=min(ans,res)
        return
    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        if(0<=xx<m and 0<=yy<n and vis[xx][yy]==0):
            vis[xx][yy]=1
            dfs(xx,yy,res+a[xx][yy],step+1)
            vis[xx][yy]=0
    return
for qaq in range(t):
    m,n=map(int,input().split())
    a=[["" for _ in range(n)]for _ in range(m)]
    vis=[[0 for _ in range(n)]for _ in range(m)]
    for i in range(m):
        for j in range(n):
            a[i][j]=chr(ord("A")+j)+str(i+1)
    ans="Z26"*26
    vis[0][0]=1
    dfs(0,0,"A1",1)
    print(f"Scenario #{qaq+1}:")
    if(ans=="Z26"*26):
        print("impossible")
    else:
        print(ans)
    print()