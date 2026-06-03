t=int(input())
def find(x):
    if(x==fa[x]):
        return x
    fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    if(find(x)!=find(y)):
        fa[find(x)]=find(y)
for _ in range(t):
    n,m=map(int,input().split())
    fa=[_ for _ in range(n+1)]
    for i in range(m):
        x,y=map(int,input().split())
        merge(x,y)
    ans=[]
    for i in range(1,n+1):
        ans.append(find(i))
    print(" ".join(map(str,ans)))