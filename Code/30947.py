import sys
from math import sqrt
from bisect import bisect_left
from functools import lru_cache
n,q=map(int,input().split())
c=list(map(int,input().split()))
cnt=0
for i in range(n):
    if(c[i]==0):
        c[i]=1
    if(c[i]>1):
        cnt+=1
c.sort(reverse=True)
if(cnt>30):
    for i in range(q):
        x=int(input())
        print("No")
    sys.exit(0)
suf=[1]*(n+1)
for i in range(n-1,-1,-1):
    suf[i]=suf[i+1]*c[i]
for i in range(q):
    x=int(input())
    div=[]
    for j in range(1,int(sqrt(x))+1):
        if(x%j==0):
            div.append(j)
            if(j*j!=x):
                div.append(x//j)
    div.sort()
    @lru_cache(None)    
    def dfs(i,rem):
        global cnt
        if(i==cnt):
            return (rem==1 or n-cnt>0)
        if(suf[i]>rem):
            return False
        for d in div:
            if(d>rem):
                break
            if(d>=c[i] and rem%d==0):
                if(dfs(i+1,rem//d)):
                    return True
        return False
    dfs.cache_clear()
    if(dfs(0,x)):
        print("Yes")
    else:
        print("No")
