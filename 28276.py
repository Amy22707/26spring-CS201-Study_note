n=int(input())
fa=[i for i in range(30)]
def find(x):
    if(fa[x]==x):
        return x
    fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    fx=find(x)
    fy=find(y)
    if(fx==fy):
        return
    fa[fx]=fy
flag=1
query=[]
for i in range(n):
    s=input()
    query.append(s)
    a=ord(s[0])-ord('a')
    b=ord(s[-1])-ord('a')
    if(s[1]=='='):
        merge(a,b)
for i in range(n):
    s=query[i]
    a=ord(s[0])-ord('a')
    b=ord(s[-1])-ord('a')
    if(s[1]=='!'):
        if(find(a)==find(b)):
            flag=0
if(flag):
    print("True")
else:
    print("False")