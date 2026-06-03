from math import gcd
a=" "+input().strip()
b=" "+input().strip()
n=len(a)
m=len(b)
dp=[[0 for _ in range(m+1)]for _ in range(n+1)]#a的前i位与b的前j位能否匹配
dp[0][0]=1
for i in range(1,n):
    if(a[i]=="*"):
        dp[i][0]=dp[i-1][0]
    else:
        break
for i in range(1,n):
    if(a[i]=="*"):
        first=-1
        if(dp[i][0]):
            first=0
        else:
            for j in range(1,m):
                if(dp[i-1][j]):
                    first=j
                    break
        if(first!=-1):
            for j in range(first,m):
                dp[i][j]=1
    elif(a[i]=='?'):
        for j in range(1,m):
            dp[i][j]=dp[i-1][j-1]
    else:
        for j in range(1,m):
            dp[i][j]=dp[i-1][j-1] and a[i]==b[j]

def get_gcd(arr):
    res=arr[0]
    for i in range(1,len(arr)):
        res=gcd(res,arr[i])
    return res

if(dp[n-1][m-1]):
    print("matched")
    res=[0]*n
    i=n-1
    j=m-1
    while(i>0):
        if(a[i]=="*"):
            if(dp[i-1][j]):
                i-=1
            else:
                res[i]+=1
                j-=1
        else:
            res[i]+=1
            i-=1
            j-=1
    s=[]
    cur=0
    for i in range(1,n):
        if(a[i]=="*" or a[i]=='?'):
            if(i>1 and a[i]!=a[i-1] and cur>0):
                s.append(cur)
                cur=0
            cur+=res[i]
        else:
            if(cur>0):
                s.append(cur)
                cur=0
    if(cur>0):
        s.append(cur)
    if(len(s)==0):
        print(0)
    else:
        print(sum(s)//get_gcd(s))
else:
    print("not matched")