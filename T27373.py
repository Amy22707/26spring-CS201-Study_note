from functools import cmp_to_key
def cmp(x,y):
    if(x+y<y+x):
        return 1
    elif(x+y==y+x):
        return 0
    else:
        return -1
def f(x):
    if(x==""):
        return 0
    else:
        return int(x)
m=int(input())
n=int(input())
a=sorted(list(input().split()),key=cmp_to_key(cmp))
dp=[["" for _ in range(m+1)]for _ in range(n)]#考虑前i个数，组成不超过j位的最大值
for j in range(len(a[0]),m+1):
    dp[0][j]=a[0]
for j in range(1,m+1):
    for i in range(1,n):
        if(len(a[i])>j):
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=str(max(f(dp[i-1][j]),f(dp[i-1][j-len(a[i])]+a[i])))
print(dp[n-1][m])