n=int(input())
s=[]
cnt=0
res=1
for i in range(2*n):
    a=input()
    if(a[0]=='a'):
        op,num=a.split()
        s.append(int(num))
    else:
        if(s and s[-1]==res):
            s.pop()
            res+=1
        elif(len(s)==0):
            res+=1
            continue
        else:
            cnt+=1
            s.clear()
            res+=1
print(cnt)
