n=int(input())
x0,y0=map(int,input().split())
vis=[[0 for _ in range(n)]for _ in range(n)]
vis[x0][y0]=1
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[-1,-2,-2,-1,1,2,2,1]
flag=0
def get_degree(x,y):
    degree=0
    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n and vis[xx][yy]==0):
            degree+=1
    return degree
def get_dist(x,y):
    return (x-n/2.0)**2+(y-n/2.0)**2
def dfs(x,y,step):
    global flag
    if(step==n*n):
        flag=1
        return
    candidates=[]
    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n and vis[xx][yy]==0):
            candidates.append((get_degree(xx,yy),-get_dist(xx,yy),xx,yy))
    candidates.sort()
    for _,__,xx,yy in candidates:
        vis[xx][yy]=1
        dfs(xx,yy,step+1)
        if(flag==1):
            return
        vis[xx][yy]=0
dfs(x0,y0,1)
if(flag==1):
    print("success")
else:
    print("fail")