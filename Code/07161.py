from collections import deque
class TreeNode:
    def __init__(self,x,):
        self.val=x
        self.children=[]
def postorder(root):
    if(root is None):
        return []
    for child in root.children:
        postorder(child)
    res.append(root.val)
    return res
n=int(input())
ans=[]
for qaq in range(n):
    s=list(input().split())
    t=len(s)
    t//=2
    nodes=[]
    deg=[]
    for qwq in range(t):
        nodes.append(s[qwq*2])
        deg.append(int(s[qwq*2+1]))
    q=deque()
    root=TreeNode(nodes[0])
    degree0=deg[0]
    q.append((root,degree0))
    cur=0
    while(q):
        n=len(q)
        for i in range(n):
            node,degree=q.popleft()
            for j in range(cur+1,cur+degree+1):
                child=TreeNode(nodes[j])
                node.children.append(child)
                q.append((child,deg[j]))
            cur+=degree
    res=[]
    ans.extend(postorder(root))
print(" ".join(ans))

