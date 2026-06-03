n,t=map(int,input().split())
s=list(map(int,input().split()))
a=[]
for i in range(n):
    a.append((s[i],i+1))
a=sorted(a,key=lambda x:(x[0],x[1]))
i=0
j=n-1
while(i<j):
    if(a[i][0]+a[j][0]<t):
        i+=1
    elif(a[i][0]+a[j][0]>t):
        j-=1
    else:
        while(a[j-1][0]==a[j][0] and j-1>i):
            j-=1
        break
print(min(a[i][1],a[j][1]),max(a[i][1],a[j][1]))