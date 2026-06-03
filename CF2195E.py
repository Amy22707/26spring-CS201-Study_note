import sys
mod=1000000007
# sys.setrecursionlimit(10**7)
# def postorder(root):
#     if(left[root]==0 and right[root]==0):
#         dp[root]=1
#         return 1
#     l,r=left[root],right[root]
#     postorder(l)
#     postorder(r)
#     dp[root]=(dp[l]+dp[r]+3)%mod
# def preorder(root,parent_res):
#     res[root]=(dp[root]+parent_res)%mod
#     l,r=left[root],right[root]
#     if(l==0 and r==0):
#         return
#     preorder(l,res[root])
#     preorder(r,res[root])
T=int(input())
for _ in range(T):
    n=int(input())
    left=[0]*(n+1)
    right=[0]*(n+1)
    dp=[0]*(n+1)
    res=[0]*(n+1)
    for i in range(1,n+1):
        l,r=map(int,input().split())
        left[i]=l
        right[i]=r
    #postorder(1)
    stack=[1]
    vis_order=[]
    while(stack):
        u=stack.pop()
        if(u==0):
            continue
        vis_order.append(u)
        stack.append(left[u])
        stack.append(right[u])#根右左
    for u in reversed(vis_order):
        l,r=left[u],right[u]
        if(l==0 and r==0):
            dp[u]=1
        else:
            dp[u]=(dp[l]+dp[r]+3)%mod
    #preorder(1,0)
    res[1]=dp[1]
    stack=[1]
    while(stack):
        u=stack.pop()
        l,r=left[u],right[u]
        if(l==0 and r==0):
            continue
        if(l!=0):
            res[l]=(dp[l]+res[u])%mod
            stack.append(l)
        if(r!=0):
            res[r]=(dp[r]+res[u])%mod
            stack.append(r)
    print(" ".join(map(str,res[1:n+1])))