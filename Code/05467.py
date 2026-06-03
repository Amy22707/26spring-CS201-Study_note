from collections import defaultdict
qaq=int(input())
for _ in range(qaq):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    n=len(a)
    n//=2
    m=len(b)
    m//=2
    d=defaultdict(int)
    for i in range(n):
        if(a[2*i+1]<0):
            break
        d[a[2*i+1]]+=a[2*i]
    for i in range(m):
        if(b[2*i+1]<0):
            break
        d[b[2*i+1]]+=b[2*i]
    ans=dict(sorted(d.items(),key=lambda x:-x[0]))
    res=[]
    for k,v in ans.items():
        if(v==0):
            continue
        res.append(f"[ {v} {k} ]")
    print(" ".join(res))