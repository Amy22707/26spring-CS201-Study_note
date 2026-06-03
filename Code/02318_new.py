while(True):
    s=input()
    if(s=='0'):
        break
    n,m,x1,y1,x2,y2=map(int,s.split())
    d={}
    res={}
    # test if y1==y2
    #(0,x1)
    for i in range(0,n):
        u,l=map(int,input().split())
        d[i]=(u,l,)#x=ky+b
    d[n]=(x2,x2)
    for i in range(n+1):
        res[i]=0
    for i in range(m):
        x,y=map(int,input().split())
        #边界x线段（从上往下），为负则在左侧，为正则在右侧
        left=0
        right=n
        ans=-1
        while(left<=right):
            mid=(left+right)>>1
            u,l=d[mid]#(u-l,y1-y2)x(u-x,y1-y)
            cross=(u-l)*(y1-y)-(y1-y2)*(u-x)
            if(cross<=0):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        res[ans]+=1
    for i in range(n+1):
        print(f"{i}: {res[i]}")
    print()