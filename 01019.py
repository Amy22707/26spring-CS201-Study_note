from math import log
from bisect import bisect_left
t=int(input())
digit=[0]*35000
sum=[0]*35000
sum[1]=1
pre=[0,1]
for i in range(1,35000):
    digit[i]=len(str(i))
for i in range(2,35000):
    sum[i]=sum[i-1]+digit[i]
    pre.append(pre[i-1]+sum[i])
for _ in range(t):
    n=int(input())
    ans=bisect_left(pre,n)
    tmp=n-pre[ans-1]
    for i in range(1,ans+1):
        tmp-=digit[i]
        if(tmp<=0):
            tmp+=digit[i]
            print(str(i)[tmp-1])
            break