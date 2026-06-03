def dfs(node):
    temp=[node]
    for i in adj[node]:
        temp.append(i)
    temp.sort()
    for i in temp:
        if(i==node):
            print(i)
        else:
            dfs(i)
n=int(input())
adj={}
all_nodes=set()
children_nodes=set()
for i in range(n):
    temp=list(map(int,input().split()))
    val=temp[0]
    adj[val]=temp[1:]
    all_nodes.add(val)
    for j in temp[1:]:
        children_nodes.add(j)
root=list(all_nodes-children_nodes)[0]
dfs(root)