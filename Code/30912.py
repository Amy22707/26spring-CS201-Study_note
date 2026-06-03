from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None,sum=0):
        self.val=val
        self.left=left
        self.right=right
        self.sum=sum
def insert(root,val):
    if(root is None):
        return TreeNode(val)
    if(val<root.val):
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root
n=int(input())
a=list(map(int,input().split()))
root=TreeNode(a[0])
for i in range(1,n):
    insert(root,a[i])
tot=0
def dfs(root):
    global tot
    if(root is None):
        return 0
    dfs(root.right)
    tot+=root.val
    root.sum=tot
    dfs(root.left)
dfs(root)
q=deque()
q.append(root)
ans=[]
while(q):
    node=q.popleft()
    ans.append(node.sum)
    if(node.left):
        q.append(node.left)
    if(node.right):
        q.append(node.right)
print(*ans)