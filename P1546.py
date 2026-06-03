import sys
n=int(input())
lst=sys.stdin.read().strip().split()
edges=[]
for i in range(n):
    for j in range(i+1,n):
        idx=i*n+j
        edges.append((int(lst[idx]),i,j))
edges.sort()
m=len(edges)
fa=[i for i in range(n)]
size=[1]*n
def find(x):
    if(fa[x]!=x):
        fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    fx=find(x)
    fy=find(y)
    if(fx!=fy):
        if(size[fx]>size[fy]):
            fx,fy=fy,fx
        fa[fx]=fy
        size[fy]+=size[fx]
ans=0
i=0
cnt=0
for i in range(m):
    w,x,y=edges[i]
    if(find(x)!=find(y)):
        merge(x,y)
        ans+=w
        cnt+=1
        if(cnt==n-1):
            break
print(ans)