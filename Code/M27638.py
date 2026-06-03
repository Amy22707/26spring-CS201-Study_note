n=int(input())
tree=[]
child=set()
leaves=0
for i in range(n):
    x,y=map(int,input().split())
    tree.append([x,y])
    child.add(x)
    child.add(y)
    if(x==-1 and y==-1):
        leaves+=1
for i in range(n):
    if(i not in child):
        root=i
        break
dep=0
def dfs(node,parent,cur):
    global dep
    if(tree[node][0]==-1 and tree[node][1]==-1):
        dep=max(dep,cur)
        return
    for i in tree[node]:
        if(i!=parent and i!=-1):
            dfs(i,node,cur+1)
dfs(root,-1,0)
print(dep,leaves)