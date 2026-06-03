n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
vis=[[0 for _ in range(m)]for _ in range(n)]
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def dfs(flag,x,y):
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if(0<=xx<n and 0<=yy<m):
            if(vis[xx][yy]==0 and a[xx][yy]==1):
                vis[xx][yy]=1
                a[xx][yy]=flag
                dfs(flag,xx,yy)
                
for i in range(n):
    if(a[i][0]==1 and vis[i][0]==0):
        vis[i][0]=1
        dfs(1,i,0)
    if(a[i][m-1]==1 and vis[i][m-1]==0):
        vis[i][m-1]=1
        dfs(1,i,m-1)
for i in range(m):
    if(a[0][i]==1 and vis[0][i]==0):
        vis[0][i]=1
        dfs(1,0,i)
    if(a[n-1][i]==1 and vis[n-1][i]==0):
        vis[n-1][i]=1
        dfs(1,n-1,i)
for i in range(1,n-1):
    for j in range(1,m-1):
        if(a[i][j]==1 and vis[i][j]==0):
            a[i][j]=0
            vis[i][j]=1
            dfs(0,i,j)
for i in range(n):
    print(*a[i])