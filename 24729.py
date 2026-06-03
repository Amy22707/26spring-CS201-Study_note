class TreeNode:
    def __init__(self,val=0,children=[]):
        self.val=val
        self.children=children
def preorder(node):
    if(node==None):
        return []
    res=[node.val]
    for i in node.children:
        res+=preorder(i)
    return res
def postorder(node):
    if(node==None):
        return []
    res=[]
    for i in node.children:
        res+=postorder(i)
    res.append(node.val)
    return res
a=input()
s=[]
n=len(a)
for i in a:
    if(ord('A')<=ord(i)<=ord('Z')):
        s.append(TreeNode(i))
    elif(i=='('):
        s.append(i)
    elif(i==')'):
        temp=[]
        while(s[-1]!='('):
            node=s.pop()
            temp.append(node)
        s.pop()
        s[-1].children=temp[::-1]
print(''.join(preorder(s[0])))
print(''.join(postorder(s[0])))