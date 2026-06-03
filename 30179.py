T=int(input())
def cycle(a):
    m=len(a)
    vis=bytearray(m)
    ans=0
    for i in range(m):
        if(not vis[i]):
            res=0
            j=i
            while(not vis[j]):
                vis[j]=1
                j=a[j]-1
                res+=1
            ans=(ans+res-1)&1
    return ans
for _ in range(T):
    n=int(input())
    a=[]
    tmp=1
    for i in range(n):
        t=list(map(int,input().split()))
        if(0 in t):
            t.remove(0)
            if(n%2==0):
                tmp=i
        a.extend(t)
    if((cycle(a)+tmp)&1):
        print("yes")
    else:
        print("no")