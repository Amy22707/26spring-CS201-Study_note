from collections import defaultdict
from math import inf
p=int(input())
d=defaultdict(int)
name=[]
for i in range(p):
    s=input()
    d[s]=i
    name.append(s)
a=[[inf for _ in range(p)]for _ in range(p)]
q=int(input())
next=[[0 for _ in range(p)]for _ in range(p)]
for i in range(q):
    x,y,z=input().split()
    idxx=d[x]
    idxy=d[y]
    a[idxx][idxy]=min(a[idxx][idxy], int(z))
    a[idxy][idxx]=min(a[idxy][idxx], int(z))
for i in range(p):
    for j in range(p):
        if(i!=j and a[i][j]!=inf):
            next[i][j]=j
        else:
            next[i][j]=-1
for k in range(p):
    for i in range(p):
        for j in range(p):
            if(a[i][k]+a[k][j]<a[i][j]):
                a[i][j]=a[i][k]+a[k][j]
                next[i][j]=next[i][k]
r=int(input())
for i in range(r):
    x,y=input().split()
    idxx=d[x]
    idxy=d[y]
    cur=idxx
    nxt=next[idxx][idxy]
    while(cur!=idxy):
        print(f"{name[cur]}->({a[cur][nxt]})->",end="")
        cur=nxt
        nxt=next[cur][idxy]
    print(name[idxy])