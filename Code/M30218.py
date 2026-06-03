n=int(input())
a=list(map(int,input().split()))
s=[]
for i in range(n):
    if(a[i]>0):
        s.append(a[i])
    else:
        while(s and s[-1]>0 and a[i]<0):
            if(-a[i]>=s[-1]):
                a[i]+=s[-1]
                s.pop()
            else:
                s[-1]+=a[i]
                a[i]=0
        if(a[i]<0):
            s.append(a[i])
print(len(s))
print(*s)