from collections import defaultdict
while(True):
    n,m=map(int,input().split())
    if(n==0 and m==0):
        break
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    rank=defaultdict(int)
    for i in range(n):
        for j in range(m):
            rank[a[i][j]]+=1
    maxm=max(rank.values())
    res=0
    for i in rank.values():
        if(i>res and i<maxm):
            res=i
    ans=[]
    for i in rank.keys():
        if(rank[i]==res):
            ans.append(i)
    print(" ".join(map(str,sorted(ans))))