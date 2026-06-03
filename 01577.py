class TreeNode:
    def __init__(self,val="",left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def insert(root,val):
    if(root==None):
        return TreeNode(val)
    if(val<root.val):
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root

def preorder(node):
    if(node==None):
        return []
    return [node.val]+preorder(node.left)+preorder(node.right)
qaq='*'
while(qaq=='*'):
    s=[]
    while(True):
        t=input()
        if(t=='*' or t=='$'):
            qaq=t
            break
        s.append(t)
    n=len(s)
    if(n==0):
        break
    for i in range(n-1,-1,-1):
        t=s[i]
        if(i!=n-1):
            for j in t:
                insert(root,j)
        if(i==n-1):
            root=TreeNode(t[0])
    print(''.join(preorder(root)))
