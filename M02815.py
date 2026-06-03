m=int(input())
n=int(input())
a=[]
dx=[0,-1,0,1]
dy=[-1,0,1,0]
def dfs(x,y,step):
    area=1
    for i in range(4):
        if((a[x][y]&(1<<i))==0):
            xx=x+dx[i]
            yy=y+dy[i]
            if(0<=xx<m and 0<=yy<n and vis[xx][yy]==0):
                vis[xx][yy]=1
                area+=dfs(xx,yy,step+1)
    return area
for i in range(m):
    a.append(list(map(int,input().split())))
ans=0
max_res=0
vis=[[0 for _ in range(n)]for _ in range(m)]
for i in range(m):
    for j in range(n):
        if(vis[i][j]==0):
            vis[i][j]=1
            max_res=max(max_res,dfs(i,j,1))
            ans+=1
print(ans)
print(max_res)