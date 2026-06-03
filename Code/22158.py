def dfs(a,b):
    if(not a):
        return []
    root=a[0]
    idx=b.find(root)
    left=dfs(a[1:idx+1],b[0:idx])
    right=dfs(a[idx+1:],b[idx+1:])
    return left+right+[root]
while(True):
    try:
        preorder=input()
        postorder=input()
        n=len(preorder)
        print(''.join(dfs(preorder,postorder)))
    except EOFError:
        break