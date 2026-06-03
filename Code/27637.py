class TreeNode:
    def __init__(self,val="",left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def preorder(root):
    if(root==None):
        return []
    return [root.val]+preorder(root.left)+preorder(root.right)
def inorder(root):
    if(root==None):
        return []
    return inorder(root.left)+[root.val]+inorder(root.right)
n=int(input())
for _ in range(n):
    a=input()
    s=[]
    for i in a:
        if(i==')'):
            temp=[]
            while(s and s[-1]!='('):
                temp.append(s.pop())
            s.pop()
            node=s[-1]
            # node.left=temp[-1] if 'A'<=temp[-1].val<='Z' else None
            # node.right=temp[0] if 'A'<=temp[0].val<='Z' else None
            node.left=temp[-1]
            node.right=temp[0]
        elif(i>='A' and i<='Z'):
            s.append(TreeNode(i))
        elif(i=='*'):
            s.append(None)
        else:
            s.append(i)
    root=s[0]
    print("".join(preorder(root)))
    print("".join(inorder(root)))

