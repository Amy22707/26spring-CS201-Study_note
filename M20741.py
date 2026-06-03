from collections import deque
n=int(input())
a=[]
vis=[[0 for _ in range(n)]for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
q=deque()
def dfs(x,y):
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n):
            if(vis[xx][yy]==0 and a[xx][yy]=="1"):
                vis[xx][yy]=1
                q.append((xx,yy,0))
                dfs(xx,yy)

for i in range(n):
    a.append(list(input()))
flag=0
for i in range(n):
    if(flag==1):
        break
    for j in range(n):
        if(a[i][j]=="1"):
            vis[i][j]=1
            q.append((i,j,0))
            dfs(i,j)
            flag=1
            break
for i in range(n):
    for j in range(n):
        if(vis[i][j]==1):
            a[i][j]='0'
while(q):
    x,y,dis=q.popleft()
    if(a[x][y]=="1"):
        print(dis-1)
        break
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n):
            if(vis[xx][yy]==0):
                vis[xx][yy]=1
                q.append((xx,yy,dis+1))