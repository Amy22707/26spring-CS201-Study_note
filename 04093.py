n=int(input())
files=[]
for i in range(n):
    t=list(map(int,input().split()))
    files.append(set(t[1:]))
m=int(input())
for i in range(m):
    q=list(map(int,input().split()))
    a=set(files[q.index(1)])
    b=set()
    for j in range(n):
        if(q[j]==1):
            a&=files[j]
        elif(q[j]==-1):
            b|=files[j]
    c=a-b
    if(len(c)==0):
        print("NOT FOUND")
    else:
        print(" ".join(map(str,sorted(c))))