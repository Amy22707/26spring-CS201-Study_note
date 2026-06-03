t=int(input())
for _ in range(t):
    n,x0,y0,maxs=map(int,input().split())
    p=[]
    h0=0
    for i in range(n):
        x,y,h=map(int,input().split())
        p.append([h,x,y])
    p.append([y0,x0,x0])
    p.sort(reverse=True)
    MAXM=float('inf')
    dp=[[MAXM for _ in range(2)]for _ in range(n+1)]#dp[i][0]:第i个平台左端点的最短时间，dp[i][1]:右端点
    if(p[-1][0])<=maxs:
        dp[n][0]=dp[n][1]=p[-1][0]
    for i in range(n-1,-1,-1):
        h0=p[i][0]
        curx,cury=p[i][1],p[i][2]
        flag1=0
        flag2=0
        for j in range(i+1,n+1):
            x,y,h=p[j][1],p[j][2],p[j][0]
            if(x<=curx<=y and flag1==0):
                if(h>=h0-maxs):
                    dp[i][0]=min(dp[j][0]+(curx-x),dp[j][1]+(y-curx))+(h0-h)
                flag1=1
            if(x<=cury<=y and flag2==0):
                if(h>=h0-maxs):
                    dp[i][1]=min(dp[j][0]+(cury-x),dp[j][1]+(y-cury))+(h0-h)
                flag2=1
            if(flag1&flag2):
                break
        if(flag1==0):
            if(h0<=maxs):
                dp[i][0]=h0
        if(flag2==0):
            if(h0<=maxs):
                dp[i][1]=h0
    print(min(dp[0][0],dp[0][1]))