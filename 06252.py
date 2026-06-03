a=" "+input()
b=" "+input()
n=len(a)
m=len(b)
dp=[[0 for _ in range(m)]for _ in range(n)]#a的前i位与b的前j位能否匹配
dp[0][0]=1
tag=[m]*n
for i in range(1,n):
    if(a[i]=="*" and dp[i-1][0]==1):
        dp[i][0]=1
        tag[i]=0
for i in range(1,n):
    for j in range(1,m):
        if(a[i]=="*" and tag[i-1]!=m):
            for k in range(tag[i-1],m):
                dp[i][k]=1
            continue
        elif(dp[i-1][j-1] and (a[i]==b[j] or a[i]=='*' or a[i]=='?')):
            dp[i][j]=1
        if(dp[i][j]):
            tag[i]=min(tag[i],j)
if(dp[n-1][m-1]):
    print("matched")
else:
    print("not matched")