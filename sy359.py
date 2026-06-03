class AVLNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=1
class AVLTree:
    def get_height(self,node):
        if(node==None):
            return 0
        return node.height
    def get_balance(self,node):
        if(node==None):
            return 0
        return self.get_height(node.left)-self.get_height(node.right)
    
    def right_rotate(self,y):
        x=y.left
        T2=x.right
        x.right=y
        y.left=T2
        y.height=max(self.get_height(y.left),self.get_height(y.right))+1
        x.height=max(self.get_height(x.left),self.get_height(x.right))+1
        return x
    def left_rotate(self,x):
        y=x.right
        T2=y.left
        y.left=x
        x.right=T2
        x.height=max(self.get_height(x.left),self.get_height(x.right))+1
        y.height=max(self.get_height(y.left),self.get_height(y.right))+1
        return y
    
    def insert(self,node,val):
        if(node==None):
            return AVLNode(val)
        if(val<node.val):
            node.left=self.insert(node.left,val)
        else:
            node.right=self.insert(node.right,val)
        node.height=1+max(self.get_height(node.left),self.get_height(node.right))
        balance=self.get_balance(node)

        if(balance>1 and val<node.left.val):
            return self.right_rotate(node)
        if(balance<-1 and val>node.right.val):
            return self.left_rotate(node)
        if(balance>1 and val>node.left.val):
            node.left=self.left_rotate(node.left)
            return self.right_rotate(node)
        if(balance<-1 and val<node.right.val):
            node.right=self.right_rotate(node.right)
            return self.left_rotate(node)
        return node
def dfs(node,res):
    if(node==None):
        return
    res.append(node.val)
    dfs(node.left,res)
    dfs(node.right,res)
avl=AVLTree()
root=None
n=int(input())
tree=list(map(int,input().split()))
for val in tree:
    root=avl.insert(root,val)
res=[]
dfs(root,res)
print(' '.join(map(str,res)))