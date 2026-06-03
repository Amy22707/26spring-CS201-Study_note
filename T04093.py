n=int(input())
doc=[]
res_glob=set()
for i in range(n):
    a=list(map(int,input().split()))
    s=a[0]
    t=set(a[1:])
    doc.append(t)
    res_glob|=t
m=int(input())
for i in range(m):
    w=list(map(int,input().split()))
    res=res_glob.copy()
    for j in range(n):
        if(w[j]==1):
            res&=doc[j]
    for j in range(n):
        if(w[j]==-1):
            res-=doc[j]
    ans=sorted(list(res))
    if(len(ans)==0):
        print("NOT FOUND")
    else:
        print(*ans)