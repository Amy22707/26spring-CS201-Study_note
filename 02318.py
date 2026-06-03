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
        k=(u-l)/(y1-y2)
        b=(l*y1-u*y2)/(y1-y2)
        d[i]=(u,l,k,b)#x=ky+b
    d[n]=(x2,x2,0,x2)
    for i in range(n+1):
        res[i]=0
    for i in range(m):
        x,y=map(int,input().split())
        for j in range(n+1):
            u,l,k,b=d[j]
            if(x<=max(u,l) and k*y+b>=x):
                res[j]+=1
                break
    for i in range(n+1):
        print(f"{i}: {res[i]}")
    print()