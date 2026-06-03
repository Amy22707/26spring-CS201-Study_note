from copy import deepcopy
m,n,p=map(int,input().split())
def left(b):
    a=deepcopy(b)
    global m,n
    for i in range(m):
        cur=0
        for j in range(n):
            if(a[i][j]!=0):
                a[i][cur],a[i][j]=a[i][j],a[i][cur]
                cur+=1
        for j in range(n):
            if(a[i][j]!=0 and j!=n-1 and a[i][j]==a[i][j+1]):
                a[i][j]*=2
                a[i][j+1]=0
        cur=0
        for j in range(n):
            if(a[i][j]!=0):
                a[i][cur],a[i][j]=a[i][j],a[i][cur]
                cur+=1
    return a
def right(b):
    a=deepcopy(b)
    global m,n
    for i in range(m):
        cur=n-1
        for j in range(n-1,-1,-1):
            if(a[i][j]!=0):
                a[i][cur],a[i][j]=a[i][j],a[i][cur]
                cur-=1
        for j in range(n-1,-1,-1):
            if(a[i][j]!=0 and j!=0 and a[i][j]==a[i][j-1]):
                a[i][j]*=2
                a[i][j-1]=0
        cur=n-1
        for j in range(n-1,-1,-1):
            if(a[i][j]!=0):
                a[i][cur],a[i][j]=a[i][j],a[i][cur]
                cur-=1
    return a
def up(b):
    a=deepcopy(b)
    global m,n
    for j in range(n):
        cur=0
        for i in range(m):
            if(a[i][j]!=0):
                a[cur][j],a[i][j]=a[i][j],a[cur][j]
                cur+=1
        for i in range(m):
            if(a[i][j]!=0 and i!=m-1 and a[i][j]==a[i+1][j]):
                a[i][j]*=2
                a[i+1][j]=0
        cur=0
        for i in range(m):
            if(a[i][j]!=0):
                a[cur][j],a[i][j]=a[i][j],a[cur][j]
                cur+=1
    return a
def down(b):
    a=deepcopy(b)
    global m,n
    for j in range(n):
        cur=m-1
        for i in range(m-1,-1,-1):
            if(a[i][j]!=0):
                a[cur][j],a[i][j]=a[i][j],a[cur][j]
                cur-=1   
        for i in range(m-1,-1,-1):
            if(a[i][j]!=0 and i!=0 and a[i][j]==a[i-1][j]):
                a[i][j]*=2
                a[i-1][j]=0
        cur=m-1
        for i in range(m-1,-1,-1):
            if(a[i][j]!=0):
                a[cur][j],a[i][j]=a[i][j],a[cur][j]
                cur-=1   
    return a    
def dfs(a,step):
    global ans,m,n,p
    # print("TEST",step)
    # for i in range(m):
    #     for j in range(n):
    #         print(a[i][j],end=' ')
    #     print()
    if(step==p):
        res=0
        for i in range(m):
            for j in range(n):
                res=max(res,a[i][j])
        ans=max(ans,res)
        return
    dfs(left(a),step+1)
    dfs(right(a),step+1)
    dfs(up(a),step+1)
    dfs(down(a),step+1)
    return
a=[]
ans=0
for i in range(m):
    t=list(map(int,input().split()))
    a.append(t)
dfs(a,0)
print(ans)