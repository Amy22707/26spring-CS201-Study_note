from math import log2
import sys
def solve():
    data=sys.stdin.read().split()
    if(not data):
        return
    it=iter(data)
    n=int(next(it))
    m=int(next(it))
    a=[int(next(it)) for _ in range(n)]
    st=[[0 for _ in range(int(log2(n))+1)] for _ in range(n)]#i为起点，长度为2^j
    log=[0]
    for i in range(1,n+1):
        log.append(int(log2(i)))
    for j in range(log[n]+1):
        for i in range(n-(1<<j)+1):
            if(j==0):
                st[i][j]=a[i]
            else:
                st[i][j]=max(st[i][j-1],st[i+(1<<(j-1))][j-1])
    res=[]
    for qaq in range(m):
        l=int(next(it))
        r=int(next(it))
        l-=1
        r-=1
        k=int(log[r-l+1])
        print(max(st[l][k],st[r-(1<<k)+1][k]))
if(__name__=="__main__"):
    solve()