from collections import deque
dx=[0,1,0,-1]
dy=[1,0,-1,0]
t=int(input())
for _ in range(t):
    r,c,k=map(int,input().split())
    a=[]
    for i in range(r):
        a.append(input())
    x0,y0,x1,y1=0,0,0,0
    for i in range(r):
        for j in range(c):
            if(a[i][j]=='S'):
                x0=i
                y0=j
            if(a[i][j]=='E'):
                x1=i
                y1=j
    q=deque()
    q.append((x0,y0,0))
    flag=0
    vis=[[[0 for _ in range(k)]for _ in range(c)]for _ in range(r)]
    vis[x0][y0][0]=1
    while(q):
        x,y,time=q.popleft()
        if(x==x1 and y==y1):
            print(time)
            flag=1
            break
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if(0<=xx<r and 0<=yy<c):
                if(vis[xx][yy][(time+1)%k]==0):
                    if((time+1)%k==0 or a[xx][yy]!='#'):
                        q.append((xx,yy,time+1))
                        vis[xx][yy][(time+1)%k]=1
    if(flag==0):
        print("Oop!")