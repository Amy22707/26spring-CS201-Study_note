def doit(n,x,a):
    s=sum(a)
    if(s%x!=0):
        return n
    else:
        i=0
        j=n-1
        si=sj=0
        while(i<n and j>=0):
            si+=a[i]
            sj+=a[j]
            if(si%x!=0 or sj%x!=0):
                return j
            i+=1
            j-=1
    return -1
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    print(doit(n,x,a))
    