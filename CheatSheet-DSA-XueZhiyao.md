## 1.数据结构
#### 1.链表
相交链表
`from typing import Optional`:返回目标类型或None
一个链表为a+c，另一个链表为b+c。走完一个开始走另一个，最终两个指针都走a+b+c，并在相交点相遇。
```python
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

a=[4,1,8,4,5]
b=[5,6,1,8,4,5] 
# 注意：这里直接生成的b包含后续节点，但为了模拟相交，我们会把b的尾部截断并接上a的相交部分
headA = create_linked_list(a)
headB = create_linked_list(b[:3]) # 只生成 [5,6,1]

# 模拟相交：相交点是 8
# a中8的位置是索引2 (4->1->8)
intersect_node = headA.next.next 

# 将b的尾部接上相交节点
curB = headB
while curB.next:
    curB = curB.next
curB.next = intersect_node

print(f"Intersect val: {Solution().getIntersectionNode(headA, headB).val}")
```
反转链表
```python
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        if(cur==None):
            return None
        qaq=cur.next
        head.next=None
        while(qaq!=None):
            tmp=qaq.next
            qaq.next=cur
            cur=qaq
            qaq=tmp
        return cur
def init(arr):
    head=ListNode(arr[0])
    cur=head
    for i in range(1,len(arr)):
        cur.next=ListNode(arr[i])
        cur=cur.next
    return head
arr=[1,2,3,4,5]
print(Solution().reverseList(init(arr)).val)
```
判断环形链表及入环口：快慢指针
```python
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        if(fast==None):
            return None
        if(fast.next==None):
            return None
        while(True):
            slow=slow.next
            fast=fast.next.next
            if(fast==None or fast.next==None):
                return None
            if(fast==slow):
                break
        cur=head
        while(slow!=cur):
            slow=slow.next
            cur=cur.next
        return cur
```
两两交换链表中的节点
```python
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return None
        if(head.next==None):
            return head
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        while(cur.next!=None and cur.next.next!=None):
            cur1=cur.next
            cur2=cur.next.next
            cur1.next=cur2.next
            cur2.next=cur1
            cur.next=cur2
            cur=cur1
        return dummy.next

```
#### 2.树状数组
单点修改，区间查询
```python
class NumArray:

    def __init__(self, nums: list[int]):
        n=len(nums)
        self.num=nums
        self.tree=[0]*(n+1)
        for i in range(n):
            self.add(i+1,nums[i])
    def lowbit(x):
        return x&(-x)
    def add(self,idx,val):
        while(idx<len(self.tree)):
            self.tree[idx]+=val
            idx+=NumArray.lowbit(idx)
    def prefix(self,index):
        ans=0
        while(index>0):
            ans+=self.tree[index]
            index-=NumArray.lowbit(index)
        return ans
    def update(self, index: int, val: int) -> None:
        self.add(index+1,val-self.num[index])
        self.num[index]=val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix(right+1)-self.prefix(left)
```
树状数组求逆序对
数字华容道
```python
def lowbit(x):
    return x&(-x)
class BIT:
    def __init__(self,n):
        self.n=n
        self.tree=[0]*(n+1)
    def update(self,idx,x):
        while(idx<=self.n):
            self.tree[idx]+=x
            idx+=lowbit(idx)
    def query(self,idx):
        ans=0
        while(idx>0):
            ans+=self.tree[idx]
            idx-=lowbit(idx)
        return ans
n=int(input())
a=[]
for i in range(n):
    t=list(map(int,input().split()))
    if(0 in t):
        tmp=i
        t.remove(0)
    a.extend(t)
m=n*n-1
b=BIT(m)
ans=0
for i in range(m-1,-1,-1):
    ans+=b.query(a[i]-1)
    b.update(a[i],1)
if(n%2==0):
    ans+=(n-tmp-1)
    if(ans%2==0):
        print("yes")
    else:
        print("no")
else:
    if(ans%2==0):
        print("yes")
    else:
        print("no")
```
#### 3.LRU缓存
```python
class Node:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache=dict()
        self.capacity=capacity
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if(key not in self.cache):
            return -1
        node=self.cache[key]
        self.remove_node(node)
        self.add_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            node=self.cache[key]
            node.val=value
            self.remove_node(node)
            self.add_to_end(node)
        else:
            node=Node(key,value)
            self.cache[key]=node
            self.add_to_end(node)
        if(len(self.cache)>self.capacity):
            self.cache.pop(self.head.next.key)
            self.remove_node(self.head.next)

    def remove_node(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def add_to_end(self,node):
        node.prev=self.tail.prev
        node.prev.next=node
        node.next=self.tail
        self.tail.prev=node
```

```python
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.od=OrderedDict()
        self.capacity=capacity
    def get(self, key: int) -> int:
        if(key not in self.od):
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if(key in self.od):
            self.od.move_to_end(key)
        self.od[key]=value
        if(len(self.od)>self.capacity):
            self.od.popitem(last=False)
```
#### 4.ST表&RMQ问题
```python
from math import log2
import sys
def solve():
    data=sys.stdin.read().split()
    if(not data):
        return
    it=iter(data)
    n=int(next(it))
    m=int(next(it))
    a=[int(next(it)) for _ in range(n)]
    st=[[0 for _ in range(int(log2(n))+1)] for _ in range(n)]#i为起点，长度为2^j
    log=[0]
    for i in range(1,n+1):
        log.append(int(log2(i)))
    for j in range(log[n]+1):
        for i in range(n-(1<<j)+1):
            if(j==0):
                st[i][j]=a[i]
            else:
                st[i][j]=max(st[i][j-1],st[i+(1<<(j-1))][j-1])
    res=[]
    for qaq in range(m):
        l=int(next(it))
        r=int(next(it))
        l-=1
        r-=1
        k=int(log[r-l+1])
        print(max(st[l][k],st[r-(1<<k)+1][k]))
if(__name__=="__main__"):
    solve()
```
5.并查集
种类并查集-虫子的生活（dfs染色）
```python
t=int(input())
for qaq in range(1,t+1):
    n,m=map(int,input().split())
    fa=[i for i in range(2*n+2)]
    siz=[1]*(2*n+2)
    def find(x):
        if(fa[x]==x):
            return x
        fa[x]=find(fa[x])
        return fa[x]
    def merge(x,y):
        fx=find(x)
        fy=find(y)
        if(fx==fy):
            return
        if(siz[fx]>siz[fy]):
            fx,fy=fy,fx
        fa[fx]=fy
        siz[fy]+=siz[fx]
    flag=0
    for i in range(m):
        x,y=map(int,input().split())
        if(flag==1):
            continue
        if(find(x)==find(y)):
            flag=1
            continue
        merge(x,y+n)
        merge(x+n,y)
    print(f"Scenario #{qaq}:")
    if(flag==0):
        print("No suspicious bugs found!")
    else:
        print("Suspicious bugs found!")
    print()
```
按秩合并-猫猫搭积木
```python
n,q,s=map(int,input().split())
fa=[i for i in range(n+1)]
siz=[1]*(n+1)
group=[set([i]) for i in range(n+1)]
ans=n
def find(x):
    if(fa[x]==x):
        return x
    fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    global ans
    fx=find(x)
    fy=find(y)
    if(fx==fy):
        return
    if(siz[fx]<siz[fy]):
        fx,fy=fy,fx
    fa[fy]=fx
    siz[fx]+=siz[fy]
    group[fx]|=group[fy]
    ans-=1
for i in range(q):
    x,y=map(int,input().split())
    merge(x,y)
    fx=find(x)
    if(siz[fx]>=s):
        ans+=siz[fx]-1
        for j in group[fx]:
            if(j==fx):
                continue
            fa[j]=j
            siz[j]=1
            group[j]=set([j])
        fa[fx]=fx
        siz[fx]=1
        group[fx]=set([fx])
    print(ans)
    # for j in range(1,n+1):
    #     print(find(j),end=" ")

```
## 2.树

寻找根节点的方法：1.找入度为零的点  
2.包含所有点的集合与包含所有子节点集合的差集
#### 1.二叉树的前/中/后序遍历
迭代/递归
中序：
```python
from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(node):
            if(node is None):
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        s=[]
        node=root
        while(node is not None or len(s)>0):
            while(node is not None):
                s.append(node)
                node=node.left
            node=s.pop()
            res.append(node.val)
            node=node.right
        return res
```
前序：
```python
def preorder_recursive(root):
    res = []   
    def dfs(node):
        if not node:
            return
        res.append(node.val)      # 根
        dfs(node.left)            # 左
        dfs(node.right)           # 右
    
    dfs(root)
    return res
    
def preorder_iterative2(root):
    res = []
    stack = []
    node = root    
    while node or stack:
        while node:
            res.append(node.val)    # 遇到节点就访问
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res
```
后序：
```python
def postorder_recursive(root):
    res = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)            # 左
        dfs(node.right)           # 右
        res.append(node.val)      # 根  
    dfs(root)
    return res
    
def postorder_iterative(root):
    if not root:
        return [] 
    res = []
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)        # 反着存（根→右→左） 
        # 先左后右，这样stack2会按 根右左 的顺序
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right) 
    # 反转得到 左右根
    while stack2:
        res.append(stack2.pop().val)
    
    return res
    
def postorder_iterative_single_stack(root):
    res = []
    stack = []
    node = root
    prev = None  # 记录上一次访问的节点
    while node or stack:
        # 一直往左走
        while node:
            stack.append(node)
            node = node.left    
        # 看栈顶节点
        peek = stack[-1]  
        # 如果右子树存在且没被访问过，转向右子树
        if peek.right and prev != peek.right:
            node = peek.right
        else:
            # 右子树为空或已访问，访问当前节点
            res.append(peek.val)
            prev = stack.pop()
    return res
```
根据二叉树前中序序列建树
```python
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
```
二叉树的最大深度
```python
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
```
翻转二叉树
```python
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(root==None):
            return None
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
```
求解二叉树里节点值之和等于 `targetSum` 的路径的数目
dfs->前缀和。 使用哈希表存储前缀和出现的次数，遍历到每一个都判断是否可以对答案造成贡献。
```python
# Definition for a binary tree node.
from typing import Optional
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt=defaultdict(int)
        cnt[0]=1
        ans=0
        def dfs(node,cur_sum):
            nonlocal ans
            if(not node):
                return
            cur_sum+=node.val
            ans+=cnt[cur_sum-targetSum]
            cnt[cur_sum]+=1
            dfs(node.left,cur_sum)
            dfs(node.right,cur_sum)
            cnt[cur_sum]-=1
        dfs(root,0)
        return ans
```
#### 2.二叉树的层序遍历
```python
from typing import Optional,List
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        res=[]
        if(root):
            q.append(root)
        while(q):
            n=len(q)
            ans=[]
            for i in range(n):
                node=q.popleft()
                if(node is None):
                    continue
                ans.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            res.append(ans)
        return res
```
二叉树的序列化和反序列化
```python
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if(not root):
            return "[]"
        res=[]
        q=deque()
        q.append(root)
        while(q):
            node=q.popleft()
            if(node):
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('null')
        return '['+','.join(res)+']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(data=="['null']" or data=="[]"):
            return None
        val=data[1:-1].split(',')
        root=TreeNode(int(val[0]))
        q=deque()
        q.append(root)
        i=1
        while(q):
            node=q.popleft()
            if(val[i]!="null"):
                node.left=TreeNode(int(val[i]))
                q.append(node.left)
            i+=1
            if(val[i]!="null"):
                node.right=TreeNode(int(val[i]))
                q.append(node.right)
            i+=1
        return root  
```
#### 3.二叉搜索树BST
有序数组转换：
```python
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def op(l,r):
            if(l>r):
                return None
            mid=(l+r)>>1
            root=TreeNode(nums[mid])
            root.left=op(l,mid-1)
            root.right=op(mid+1,r)
            return root
        return op(0,len(nums)-1)
```
插入建树
```python
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
```
第k小的元素：中序遍历
```python
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s=[]
        while(root!=None or len(s)!=0):
            while(root!=None):
                s.append(root)
                root=root.left
            root=s.pop()
            k-=1
            if(k==0):
                return root.val
            root=root.right
print(Solution().kthSmallest(TreeNode(3,TreeNode(1),TreeNode(4)),1))
```
#### 4.最近公共祖先LCA
二叉树
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(not root or root==p or root==q):
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if(left and right):
            return root
        if(left):
            return left
        if(right):
            return right
        return None
```
最深叶节点的最近公共祖先
```python
from typing import Optional,List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if(node is None):
                return (None,0)
            lca_left,depth_left=dfs(node.left)
            lca_right,depth_right=dfs(node.right)
            if(depth_left==depth_right):
                return (node,depth_left+1)
            elif(depth_left>depth_right):
                return (lca_left,depth_left+1)
            elif(depth_left<depth_right):
                return (lca_right,depth_right+1)
        return dfs(root)[0]
```
dfn
```python
from math import log2
import sys
sys.setrecursionlimit(10**7)
n,m,root=map(int,input().split())
tree=[[] for _ in range(n+1)]
dfn=[0]*(n+1)
dep=[0]*(n+1)
seq=[0]*(n+1)#seq[dfn[i]]
p=[0]*(n+1)
timer=0
def dfs(parent,node,depth):
    global timer
    timer+=1
    dfn[node]=timer
    seq[timer]=node
    p[node]=parent
    dep[node]=depth
    for i in tree[node]:
        if(i!=parent):
            dfs(node,i,depth+1)
for i in range(n-1):
    x,y=map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)
dep[0]=dfn[0]=float('inf')
dfs(0,root,0)
log=[0]*(n+1)
for i in range(1,n+1):
    log[i]=int(log2(i))
st=[[0 for _ in range(log[n]+1)] for _ in range(n+1)]
for i in range(1,n+1):
    st[i][0]=seq[i]
for j in range(1,log[n]+1):
    for i in range(1,n-(1<<j)+2):
        if(dep[st[i][j-1]]<dep[st[i+(1<<(j-1))][j-1]]):
            st[i][j]=st[i][j-1]
        else:
            st[i][j]=st[i+(1<<(j-1))][j-1]
def lca(x,y):
    if(x==y):
        return x
    l=dfn[x]
    r=dfn[y]
    if(l>r):
        l,r=r,l
    l+=1
    k=log[r-l+1]
    a=st[l][k]
    b=st[r-(1<<k)+1][k]
    if(dep[a]<dep[b]):
        return p[a]
    else:
        return p[b]
for _ in range(m):
    x,y=map(int,input().split())
    print(lca(x,y))
```
倍增
```python
from math import log2
import sys
sys.setrecursionlimit(10**7)
def dfs(parent,node,depth):
    p[node]=parent
    dep[node]=depth
    for i in tree[node]:
        if(i!=parent):
            dfs(node,i,depth+1)
n,m,root=map(int,input().split())
tree=[[] for _ in range(n+1)]
for i in range(n-1):
    x,y=map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)
max_log=20
up=[[0 for _ in range(max_log)]for _ in range(n+1)]#i的2^j祖先
dep=[0]*(n+1)
p=[0]*(n+1)
dfs(0,root,0)
for i in range(1,n+1):
    up[i][0]=p[i]
for j in range(1,max_log):
    for i in range(1,n+1):
        up[i][j]=up[up[i][j-1]][j-1]
def lca(x,y):
    if(dep[x]<dep[y]):
        x,y=y,x
    diff=dep[x]-dep[y]
    for i in range(max_log):
        if((diff>>i)&1):
            x=up[x][i]
    if(x==y):
        return x
    for i in range(max_log-1,-1,-1):
        if(up[x][i]!=up[y][i]):
            x=up[x][i]
            y=up[y][i]
    return p[x]
for _ in range(m):
    x,y=map(int,input().split())
    print(lca(x,y))
```
#### 5.堆
向下调整构建大顶堆
```python
def heapify(heap,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if(l<n and heap[l]>heap[largest]):
        largest=l
    if(r<n and heap[r]>heap[largest]):
        largest=r
    if(largest!=i):
        heap[i],heap[largest]=heap[largest],heap[i]
        heapify(heap,n,largest)
n=int(input())
heap=list(map(int,input().split()))
for i in range(n//2-1,-1,-1):
    heapify(heap,n,i)
print(*heap)
```
#### 6.哈夫曼编码树
```python
import heapq
class Node:
    def __init__(self,weight,chars,left=None,right=None):
        self.weight=weight
        self.chars=sorted(list(chars))
        self.min_char=self.chars[0]
        self.left=left
        self.right=right
    def __lt__(self,other):
        if(self.weight!=other.weight):
            return self.weight<other.weight
        return self.min_char<other.min_char
def build(nodes):
    heapq.heapify(nodes)
    while(len(nodes)>1):
        left=heapq.heappop(nodes)
        right=heapq.heappop(nodes)
        new_weight=left.weight+right.weight
        new_chars=left.chars+right.chars
        parent=Node(new_weight,new_chars,left,right)
        heapq.heappush(nodes,parent)
    return nodes[0]
def decode(node,res,codes):
    if(not node.left and not node.right):
        codes[node.chars[0]]=res
        return
    if(node.left):
        decode(node.left,res+'0',codes)
    if(node.right):
        decode(node.right,res+'1',codes)

n=int(input())
nodes=[]
for i in range(n):
    char,freq=input().split()
    freq=int(freq)
    nodes.append(Node(freq,[char]))
root=build(nodes)
char_to_code={}
decode(root,'',char_to_code)
code_to_char={}
while(True):
    try:
        q=input()
        if(q[0] in "01"):
            res=""
            cur=root
            for c in q:
                if(c=='0'):
                    cur=cur.left
                else:
                    cur=cur.right
                if(not cur.left and not cur.right):
                    res+=cur.chars[0]
                    cur=root
        else:
            res=""
            for c in q:
                res+=char_to_code[c]
        print(res)
    except EOFError:
        break

```
#### 7.Trie前缀树/字典树
```python
class TreeNode:
    def __init__(self):
        self.children=[None]*26
        self.isEnd=False
class Trie:
    def __init__(self):
        self.root=TreeNode()
    def searchprefix(self,word):
        node=self.root
        for c in word:
            idx=ord(c)-ord('a')
            if(node.children[idx]==None):
                return None
            node=node.children[idx]
        return node
    
    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            idx=ord(c)-ord('a')
            if(node.children[idx]==None):
                node.children[idx]=TreeNode()
            node=node.children[idx]
        node.isEnd=True

    def search(self, word: str) -> bool:
        node=self.searchprefix(word)
        return node!=None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchprefix(prefix) != None
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```
#### 8.线段树
单点修改+区间查询
```python
class NumArray:
    def __init__(self, nums: list[int]):
        self.n=len(nums)
        self.nums=nums
        self.tree=[0]*(self.n*4)
        self.build(1,0,self.n-1)
        
    def build(self,node,l,r):
        if(l==r):
            self.tree[node]=self.nums[l]
            return
        mid=(l+r)>>1
        self.build(node*2,l,mid)
        self.build(node*2+1,mid+1,r)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]

    def update_tree(self,node,l,r,idx,val):
        if(l==r):
            self.tree[node]=val
            self.nums[idx]=val
            return
        mid=(l+r)>>1
        if(idx<=mid):
            self.update_tree(node*2,l,mid,idx,val)
        else:
            self.update_tree(node*2+1,mid+1,r,idx,val)
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1] 

    def update(self, index: int, val: int) -> None:
        self.update_tree(1,0,self.n-1,index,val)

    def sums(self,node,start,end,l,r):#l-r目标区间，start-end当前区间
        if(l<=start and end<=r):
            return self.tree[node]
        if(end<l or start>r):
            return 0
        mid=(start+end)>>1
        return self.sums(node*2,start,mid,l,r)+self.sums(node*2+1,mid+1,end,l,r)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.sums(1,0,self.n-1,left,right)

```
区间修改+区间查询（lazy tag)
```python
class NumArray:
    def __init__(self, nums: list[int]):
        self.n=len(nums)
        self.nums=nums
        self.tree=[0]*(self.n*4)
        self.lazy=[0]*(self.n*4)
        self.build(1,0,self.n-1)

    def pushup(self,node):
        self.tree[node]=self.tree[node*2]+self.tree[node*2+1]
    def pushdown(self,node,l,r):
        if(self.lazy[node]!=0):
            mid=(l+r)>>1
            self.tree[node*2]+=(mid-l+1)*self.lazy[node]
            self.tree[node*2+1]+=(r-mid)*self.lazy[node]
            self.lazy[node*2]+=self.lazy[node]
            self.lazy[node*2+1]+=self.lazy[node]
            self.lazy[node]=0    
    def build(self,node,l,r):
        if(l==r):
            self.tree[node]=self.nums[l]
            return
        mid=(l+r)>>1
        self.build(node*2,l,mid)
        self.build(node*2+1,mid+1,r)
        self.pushup(node)

    def update_range(self,node,start,end,l,r,val):
        if(l<=start and end<=r):
            self.tree[node]+=(end-start+1)*val
            self.lazy[node]+=val
            return
        if(end<l or start>r):
            return
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        self.update_range(node*2,start,mid,l,r,val)
        self.update_range(node*2+1,mid+1,end,l,r,val)
        self.pushup(node)

    def sums(self,node,start,end,l,r):#l-r目标区间，start-end当前区间
        if(l<=start and end<=r):
            return self.tree[node]
        if(end<l or start>r):
            return 0
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        return self.sums(node*2,start,mid,l,r)+self.sums(node*2+1,mid+1,end,l,r)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.sums(1,0,self.n-1,left,right)n
```
最大值
```python
class SegmentTree:
    def __init__(self,n,nums):
        self.n=n
        self.nums=nums
        self.tree=[0]*(n*4)
        self.lazy=[0]*(n*4)
        self.build(1,1,n)
    def pushup(self,node):
        self.tree[node]=max(self.tree[node*2],self.tree[node*2+1])
    def pushdown(self,node,l,r):
        if(self.lazy[node]!=0):
            mid=(l+r)>>1
            self.tree[node*2]+=self.lazy[node]
            self.tree[node*2+1]+=self.lazy[node]
            self.lazy[node*2]+=self.lazy[node]
            self.lazy[node*2+1]+=self.lazy[node]
            self.lazy[node]=0
    def build(self,node,l,r):
        if(l==r):
            self.tree[node]=self.nums[l]
            return
        mid=(l+r)>>1
        self.build(node*2,l,mid)
        self.build(node*2+1,mid+1,r)
        self.pushup(node)
    def update_range(self,node,start,end,l,r,val):
        if(l<=start and end<=r):
            self.tree[node]+=val
            self.lazy[node]+=val
            return
        if(end<l or start>r):
            return
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        self.update_range(node*2,start,mid,l,r,val)
        self.update_range(node*2+1,mid+1,end,l,r,val)
        self.pushup(node)
    def query(self,node,start,end,l,r):
        if(l<=start and end<=r):
            return self.tree[node]
        if(end<l or start>r):
            return 0
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        return max(self.query(node*2,start,mid,l,r),self.query(node*2+1,mid+1,end,l,r))
n,q=map(int,input().split())
tree=SegmentTree(n,[0]*(n+1))
for _ in range(q):
    s=input().split()
    op=s[0]
    if(op=='Add'):
        l,r,v=map(int,s[1:])
        tree.update_range(1,1,n,l,r,v)
    elif(op=="Query"):
        l,r=map(int,s[1:])
        print(tree.query(1,1,n,l,r))
```
排队又来了
如果i<j，且|hi−hj|>k，则hi与hj的位置不能互换。因此将hi->hj连边，所得即为DAG.根据规则，输出最小拓扑排序即可。  
考虑优化复杂度，求每个点入度时，排序并离散化，在从左往右扫描的过程中使用树状数组维护已经扫描过的高度情况。拓扑排序使用线段树优化区间修改入度，即采用线段树记录最小值，每次取根节点并二分查找需要更新入度的区间。
```python
import heapq
from bisect import bisect_right
n,k=map(int,input().split())
a=list(map(int,input().split()))
sorted_a=sorted(a)
idxa=[]
for i in range(n):
    idxa.append((a[i],i))
sorted_idxa=sorted(idxa)
rank_to_h=[0]*(n+1)#rank->高度
pos_to_rank=[0]*(n+1)#原始下标->rank
for i in range(n):
    x,idx=sorted_idxa[i]
    pos_to_rank[idx]=i+1
    rank_to_h[i+1]=x

def lowbit(x):
    return x&(-x)
bit=[0]*(n+1)
def bit_add(idx,v):
    while(idx<=n):
        bit[idx]+=v
        idx+=lowbit(idx)
def bit_query(idx):
    res=0
    while(idx>0):
        res+=bit[idx]
        idx-=lowbit(idx)
    return res
deg=[0]*(n+1)
for i in range(n):
    cur_rank=pos_to_rank[i]
    cur_h=rank_to_h[cur_rank]
    x=bisect_right(sorted_a,cur_h-k-1)
    y=bisect_right(sorted_a,cur_h+k)
    deg[cur_rank]=bit_query(x)+(i-bit_query(y))
    bit_add(cur_rank,1)
tree=[(0,0)]*(4*n)
tag=[0]*(4*n)
def build(node,l,r):
    if(l==r):
        tree[node]=(deg[l],l)
        return
    mid=(l+r)//2
    build(node*2,l,mid)
    build(node*2+1,mid+1,r)
    tree[node]=min(tree[node*2],tree[node*2+1])
def push_up(node,val):
    tag[node]+=val
    tree[node]=(tree[node][0]+val,tree[node][1])
def push_down(node):
    if(tag[node]!=0):
        push_up(node*2,tag[node])
        push_up(node*2+1,tag[node])
        tag[node]=0
def update(node,start,end,l,r,val):
    if(start>r or end<l):
        return
    if(start>=l and end<=r):
        push_up(node,val)
        return
    push_down(node)
    mid=(start+end)//2
    update(node*2,start,mid,l,r,val)
    update(node*2+1,mid+1,end,l,r,val)
    tree[node]=min(tree[node*2],tree[node*2+1])

build(1,1,n)
res=[]
maxm=10**9
for i in range(n):
    min_deg,idx=tree[1]
    res.append(rank_to_h[idx])
    update(1,1,n,idx,idx,maxm)
    h=rank_to_h[idx]
    x=bisect_right(sorted_a,h-k-1)
    y=bisect_right(sorted_a,h+k)
    if(x>=1):
        update(1,1,n,1,x,-1)
    if(y<n):
        update(1,1,n,y+1,n,-1)
print(" ".join(map(str,res)))

```
#### 9.平衡二叉树AVL
```python
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

```
#### 10.树形dp
二叉树的最大路径和
递归求解每个点的贡献（自己的值+左子树贡献+右子树贡献）。然后经过每个点的路径最大值即为自己加上左右子树的最大贡献。
```python
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxm=-float('inf')
        def maxgain(node):#以node为根,相当于node的贡献
            nonlocal maxm
            if(node is None):
                return 0
            left_gain=max(maxgain(node.left),0)
            right_gain=max(maxgain(node.right),0)
            maxm=max(maxm,node.val+left_gain+right_gain)
            return node.val+max(left_gain,right_gain)
        maxgain(root)
        return maxm
```
CF2195E
后序遍历迭代+dp数组记录每个点向下一趟之后回到原来的点的代价。
dp[root]=(dp[l]+1)+(dp[r]+1)+1=dp[l]+dp[r]+3.
```python
import sys
mod=1000000007
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

```
宝藏二叉树：不能选择相邻点的最大值
```python
n=int(input())
a=[0]+list(map(int,input().split()))
dp1=[0 for _ in range(n+1)]#以i为根，选i
dp2=[0 for _ in range(n+1)]#以i为根，不选i
for i in range(n,0,-1):
    left=i<<1
    right=(i<<1)|1
    dp1[i]=a[i]
    if(left<=n):
        dp1[i]+=dp2[left]
        dp2[i]+=max(dp1[left],dp2[left])
    if(right<=n):
        dp1[i]+=dp2[right]
        dp2[i]+=max(dp1[right],dp2[right])
print(max(dp1[1],dp2[1]))
```
#### 11.败方树
```python
from collections import deque
n,m=map(int,input().split())
a=list(map(int,input().split()))
class Node:
    def __init__(self,val=0):
        self.val=val
        self.win=val
        self.left=None
        self.right=None
        self.parent=None
leaves=[Node(x) for x in a]
q=deque(leaves)
while(len(q)>1):
    a=q.popleft()
    b=q.popleft()
    cur=Node()
    cur.val=max(a.win,b.win)
    cur.win=min(a.win,b.win)
    cur.left=a
    cur.right=b
    a.parent=b.parent=cur
    q.append(cur)
cur=q.popleft()
root=Node(cur.win)
root.left=cur
cur.parent=root
def bfs():
    res=[]
    qaq=deque()
    qaq.append(root)
    while(qaq and len(res)<n):
        cur=qaq.popleft()
        res.append(cur.val)
        if(cur.left):
            qaq.append(cur.left)
        if(cur.right):
            qaq.append(cur.right)
    return res
res=bfs()
print(*res)
for i in range(m):
    idx,val=map(int,input().split())
    cur=leaves[idx]
    cur.val=cur.win=val
    p=cur.parent
    while(p):
        if(p.right):
            p.val=max(p.left.win,p.right.win)
            p.win=min(p.left.win,p.right.win)
        else:
            p.val=p.win=p.left.win
        p=p.parent
    res=bfs()
    print(*res)
```
## 3.图
#### 1.有向图判环&拓扑排序
有向图判环，需使用三状态标记，判断下一个节点是否在当前路径上。（有可能出现访问了已经访问但不在当前路径上的节点的情况。）（三色dfs）  
无向图判环，排除是否为父节点即可。
Kahn:一个无环的有向图，必然存在至少一个入度为0的节点（没有依赖），拿掉它和它的边之后，剩下的图依然是无环的。（拓扑排序）
```python
n,m=map(int,input().split())
a=[[] for _ in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    a[u].append(v)
vis=[0]*n
flag=0
def dfs(node):
    global flag
    for c in a[node]:
        if(vis[c]==0):
            vis[c]=2
            dfs(c)
        elif(vis[c]==2):
            flag=1
            return
        vis[c]=1
for i in range(n):
    if(vis[i]==0):
        vis[i]=2
        dfs(i)
        vis[i]=1
    if(flag==1):
        break
if(flag==1):
    print("Yes")
else:
    print("No")
```

```python
from collections import deque
def has_cycle_kahn(n, edges):
    # 1. 构建邻接表和入度数组
    graph = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    # 2. 将所有入度为0的节点入队
    queue = deque([i for i in range(n) if indegree[i] == 0])
    # 3. BFS
    visited_count = 0
    while queue:
        node = queue.popleft()
        visited_count += 1
        # 删除当前节点，邻居入度减1
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    # 4. 判断：访问节点数 < n 则有环
    return visited_count != n
```
同时输出拓扑排序：
```python
def topological_sort_kahn(n, edges):
    graph = [[] for _ in range(n)]
    indegree = [0] * n 
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    queue = deque([i for i in range(n) if indegree[i] == 0])
    topo_order = []
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    # 有环返回空，无环返回拓扑序
    return topo_order if len(topo_order) == n else []
```
#### 2.最小生成树MST
Kruskal：将所有边从小到大排序，依次选择，如果边的两端已经在树上（使用并查集，联通），则跳过。  
Prim：选一个点，从连出去的边中选择最短的，把新点加入树中。之后每次选择树上的点和不在树上的点之间的最短边。
```python
import sys
n=int(input())
lst=sys.stdin.read().strip().split()
edges=[]
for i in range(n):
    for j in range(i+1,n):
        idx=i*n+j
        edges.append((int(lst[idx]),i,j))
edges.sort()
m=len(edges)
fa=[i for i in range(n)]
size=[1]*n
def find(x):
    if(fa[x]!=x):
        fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    fx=find(x)
    fy=find(y)
    if(fx!=fy):
        if(size[fx]>size[fy]):
            fx,fy=fy,fx
        fa[fx]=fy
        size[fy]+=size[fx]
ans=0
i=0
cnt=0
for i in range(m):
    w,x,y=edges[i]
    if(find(x)!=find(y)):
        merge(x,y)
        ans+=w
        cnt+=1
        if(cnt==n-1):
            break
print(ans)
```

```python
import heapq
def prim_heap(n, edges, start=0):
    # 构建邻接表
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    visited = [False] * n
    min_heap = [(0, start, -1)]  # (权重, 当前节点, 父节点)
    mst_cost = 0
    mst_edges = []
    nodes_in_mst = 0
    while min_heap and nodes_in_mst < n:
        weight, u, parent = heapq.heappop(min_heap)  
        # 跳过已访问节点（可能有旧记录在堆里）
        if visited[u]:
            continue    
        visited[u] = True
        nodes_in_mst += 1
        mst_cost += weight   
        if parent != -1:
            mst_edges.append((parent, u, weight))
        # 将邻居加入堆
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))
    # 判断是否连通
    if nodes_in_mst < n:
        return -1, []
    return mst_cost, mst_edges
```
01最小生成树
要求最小生成树即需要包含尽可能多的零边。考虑零边连接成的连通块，最终的MST即为将这些连通块连在一起，因此MST的大小即为连通块个数减1.使用bfs+差集操作避免超时。
```python
import sys
from collections import deque
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
g=set()
for i in range(m):
    x,y=map(int,input().split())
    g.add((x,y))
    g.add((y,x))
ans=0
vis=set()
for i in range(1,n+1):
    vis.add(i)
q=deque()
for i in range(1,n+1):
    if(i in vis):
        vis.remove(i)
        q.append(i)
        while(q):
            node=q.popleft()
            tmp=set()
            for j in vis:
                if((node,j) not in g):
                    tmp.add(j)
                    q.append(j)
            vis-=tmp           
        ans+=1
print(ans-1)
```
0-w最小生成树：bfs求所有连通块并标记，然后对连通块跑MST.
```python
from collections import deque
n,m=map(int,input().split())
g=[[]for _ in range(n+1)]
edges=[]
for i in range(m):
    u,v,w=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
    edges.append((w,u,v))
par=[0]*(n+1)
q=deque()
un_vis=[i for i in range(1,n+1)]
marked=[0]*(n+1)
cnt=0
while(un_vis):
    cnt+=1
    start=un_vis.pop()
    q.append(start)
    par[start]=cnt
    while(q):
        idx=q.popleft()
        for i in g[idx]:
            marked[i]=1
        nxt=[]
        for i in un_vis:
            if(marked[i]==0):
                q.append(i)
                par[i]=cnt
            else:
                nxt.append(i)
        un_vis=nxt
        for i in g[idx]:
            marked[i]=0
fa=[i for i in range(cnt+1)]
def find(x):
    if(x==fa[x]):
        return x
    fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    fx=find(x)
    fy=find(y)
    if(fx==fy):
        return
    fa[fx]=fy
new_edges=[]
for w,u,v in edges:
    if(par[u]!=par[v]):
        new_edges.append((w,par[u],par[v]))
new_edges=sorted(new_edges,key=lambda x:x[0])
ans=0
tot=cnt-1
qwq=0
for w,u,v in new_edges:
    if(qwq==tot):
        break
    if(find(u)!=find(v)):
        merge(u,v)
        ans+=w
        qwq+=1
print(ans)

```
#### 3.强连通分量SCC
Tarjan SCC缩点
校园网
```python
import sys
sys.setrecursionlimit(1000000)
n=int(input())
a=[[]]
for i in range(1,n+1):
    a.append(list(map(int,input().split()))[:-1])
dfn=[0]*(n+1)
low=[0]*(n+1)
time=0
s=[]
scc=[]
idx=[0]*(n+1)
def tarjan(k):
    global time
    time+=1
    low[k]=dfn[k]=time
    s.append(k)
    for i in a[k]:
        if(dfn[i]==0):
            tarjan(i)
            low[k]=min(low[k],low[i])
        elif(i in s):
            low[k]=min(low[k],dfn[i])
    if(low[k]==dfn[k]):
        tmp=[]
        while(True):
            x=s.pop()
            tmp.append(x)
            idx[x]=len(scc)
            if(x==k):
                break
        scc.append(tmp)
for i in range(1,n+1):
    if(dfn[i]==0):
        tarjan(i)
lens=len(scc)
in_deg=[0]*lens
out_deg=[0]*lens
for i in range(1,n+1):
    for j in a[i]:
        if(idx[i]!=idx[j]):
            out_deg[idx[i]]+=1
            in_deg[idx[j]]+=1
ans1=0
ans2=0
for i in range(lens):
    if(in_deg[i]==0):
        ans1+=1
    if(out_deg[i]==0):
        ans2+=1
print(ans1)
if(lens==1):
    print(0)
else:
    print(max(ans1,ans2))
```
缩点+拓扑序dp最大权值和
```python
from collections import deque
import sys
sys.setrecursionlimit(1000000)
n,m=map(int,input().split())
p=[0]+list(map(int,input().split()))
a=[[]for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    a[x].append(y)
dfn=[0]*(n+1)
low=[0]*(n+1)
time=0
s=[]
scc=[]
idx=[0]*(n+1)
val=[]
def tarjan(k):
    global time
    time+=1
    low[k]=dfn[k]=time
    s.append(k)
    for i in a[k]:
        if(dfn[i]==0):
            tarjan(i)
            low[k]=min(low[k],low[i])
        elif(i in s):
            low[k]=min(low[k],dfn[i])
    if(low[k]==dfn[k]):
        tmp=[]
        sum=0
        while(True):
            x=s.pop()
            tmp.append(x)
            sum+=p[x]
            idx[x]=len(scc)
            if(x==k):
                break
        scc.append(tmp)
        val.append(sum)
for i in range(1,n+1):
    if(dfn[i]==0):
        tarjan(i)
lens=len(scc)
in_deg=[0]*lens
dag=[[]for _ in range(lens)]
for i in range(1,n+1):
    for j in a[i]:
        if(idx[i]!=idx[j]):
            in_deg[idx[j]]+=1
            dag[idx[i]].append(idx[j])
q=deque()
dp=[0]*lens
for i in range(lens):
    if(in_deg[i]==0):
        q.append(i)
        dp[i]=val[i]
while(q):
    x=q.popleft()
    for i in dag[x]:
        dp[i]=max(dp[i],dp[x]+val[i])
        in_deg[i]-=1
        if(in_deg[i]==0):
            q.append(i)
print(max(dp))
```
#### 4.最短路
Dijkstra
正向+反向图
```python
import heapq
n,m=map(int,input().split())
a=[[]for _ in range(n+1)]
b=[[]for _ in range(n+1)]
for i in range(m):
    x,y,z=map(int,input().split())
    a[x].append((y,z))
    b[y].append((x,z))
dist=[float("inf") for _ in range(n+1)]
dist[1]=0
dist2=[float("inf") for _ in range(n+1)]
dist2[1]=0
h=[]
heapq.heappush(h,(0,1))
while(h):
    d,node=heapq.heappop(h)
    if(d>dist[node]):
        continue
    for nxt,cost in a[node]:
        if(dist[node]+cost<dist[nxt]):
            dist[nxt]=dist[node]+cost
            heapq.heappush(h,(dist[nxt],nxt))
h=[]
heapq.heappush(h,(0,1))
while(h):
    d,node=heapq.heappop(h)
    if(d>dist2[node]):
        continue
    for nxt,cost in b[node]:
        if(dist2[node]+cost<dist2[nxt]):
            dist2[nxt]=dist2[node]+cost
            heapq.heappush(h,(dist2[nxt],nxt))
ans=0
for i in range(1,n+1):
    ans+=dist[i]+dist2[i]
print(ans)
```
Floyd全图最短路
```python
from collections import defaultdict
from math import inf
p=int(input())
d=defaultdict(int)
name=[]
for i in range(p):
    s=input()
    d[s]=i
    name.append(s)
a=[[inf for _ in range(p)]for _ in range(p)]
q=int(input())
next=[[0 for _ in range(p)]for _ in range(p)]
for i in range(q):
    x,y,z=input().split()
    idxx=d[x]
    idxy=d[y]
    a[idxx][idxy]=min(a[idxx][idxy], int(z))
    a[idxy][idxx]=min(a[idxy][idxx], int(z))
for i in range(p):
    for j in range(p):
        if(i!=j and a[i][j]!=inf):
            next[i][j]=j
        else:
            next[i][j]=-1
for k in range(p):
    for i in range(p):
        for j in range(p):
            if(a[i][k]+a[k][j]<a[i][j]):
                a[i][j]=a[i][k]+a[k][j]
                next[i][j]=next[i][k]
r=int(input())
for i in range(r):
    x,y=input().split()
    idxx=d[x]
    idxy=d[y]
    cur=idxx
    nxt=next[idxx][idxy]
    while(cur!=idxy):
        print(f"{name[cur]}->({a[cur][nxt]})->",end="")
        cur=nxt
        nxt=next[cur][idxy]
    print(name[idxy])

```
SPFA带负权单源最短路
```python
def spfa_with_path(n, edges, start):
    """返回最短距离和路径"""
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0
    parent = [-1] * n
    
    in_queue = [False] * n
    cnt = [0] * n
    
    queue = deque([start])
    in_queue[start] = True
    cnt[start] = 1
    
    while queue:
        u = queue.popleft()
        in_queue[u] = False
        
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
                    cnt[v] += 1
                    if cnt[v] >= n:
                        return dist, parent, True
    
    return dist, parent, False

# 还原路径
def get_path(parent, start, end):
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]
```
Bellman-Ford
```python
def bellman_ford_with_path(n, edges, start):
    """返回最短距离、路径和负环信息"""
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0
    parent = [-1] * n
    
    # n-1 轮松弛
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break
    
    # 检测负环
    negative_cycle_node = -1
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
            negative_cycle_node = v  # 负环上的一个节点
    
    has_cycle = negative_cycle_node != -1
    
    return dist, parent, has_cycle, negative_cycle_node


def reconstruct_path(parent, start, end):
    """还原最短路径"""
    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]
```
同余最短路
upstaris
选择a,b,c中最小的数（不妨a）作为最后叠加的层数，问题转化为在模a意义下，h=by+cz，而当此时的h最小，它是否小于目标的h。因此对每个余数u构建(u+b) mod a和(u+c) mod a的路径，从0开始跑一遍Dijkstra，得到的即为最小的h.
```python
import heapq
a,b,c=map(int,input().split())
query=int(input())
step=[]
if(a>0):
    step.append(a)
if(b>0):
    step.append(b)
if(c>0):
    step.append(c)
step.sort()
if(len(step)>=2):
    m=step[0]
    edges=step[1:]
    dist=[float("inf")]*m
    dist[0]=0
    q=[]
    heapq.heappush(q,(0,0))
    while(q):
        d,node=heapq.heappop(q)
        if(d>dist[node]):
            continue
        for i in edges:
            nxt=(node+i)%m
            if(dist[nxt]>d+i):
                dist[nxt]=d+i
                heapq.heappush(q,(dist[nxt],nxt))
def solve(h):
    if(len(step)==0):
        if(h==0):
            return True
        else:
            return False
    elif(len(step)==1):
        if(h%step[0]==0):
            return True
        else:
            return False
    rem=h%m
    if(dist[rem]<=h):
        return True
    else:
        return False
for i in range(query):
    h=int(input())
    if(solve(h)):
        print("Yes")
    else:
        print("No")

```
#### 5.关键路径AOE
根据入度和出度进行正向和反向拓扑排序，以此更新节点最早开始时间和最晚开始时间。关键路径长度即为所有节点最早开始时间的最大值。对于每条边，如果起点的最早开始时间加工程长度等于终点的最晚开始时间，那么它是关键活动，开始时间必须确定。
```python
from collections import deque
n,m=map(int,input().split())
g=[[]for _ in range(n+1)]
r=[[]for _ in range(n+1)]
in_deg=[0]*(n+1)
out_deg=[0]*(n+1)
for i in range(m):
    x,y,z=map(int,input().split())
    g[x].append((y,z))
    r[y].append((x,z))
    in_deg[y]+=1
    out_deg[x]+=1
q=deque()
ve=[0]*(n+1)
for i in range(1,n+1):
    if(in_deg[i]==0):
        q.append(i)
while(q):
    node=q.popleft()
    for i,val in g[node]:
        ve[i]=max(ve[i],ve[node]+val)
        in_deg[i]-=1
        if(in_deg[i]==0):
            q.append(i)

ans=max(ve)
print(ans)
vl=[ans]*(n+1)
q=deque()
for i in range(1,n+1):
    if(out_deg[i]==0):
        q.append(i)
while(q):
    node=q.popleft()
    for i,val in r[node]:
        vl[i]=min(vl[i],vl[node]-val)
        out_deg[i]-=1
        if(out_deg[i]==0):
            q.append(i)
res=[]
for i in range(1,n+1):
    for j,k in g[i]:
        if(ve[i]+k==vl[j]):
            res.append((i,j))
res.sort()
for i,j in res:
    print(i,j)
```
#### 6.欧拉路
对每个单词建立从第一个字母指向最后一个字母的有向边，题目转化为求欧拉路径。通过入度与出度判断是否存在合法的路径以及起点，然后使用Hierholzer算法，dfs搜索，每次经过一条边即删除，并在当前点无出边时将该点倒序加入答案路径。
```python
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
t=int(input())
for _ in range(t):
    n=int(input())
    words=[]
    for i in range(n):
        tmp=input()
        words.append(tmp)
    words.sort()
    a=defaultdict(list)
    in_deg=defaultdict(int)
    out_deg=defaultdict(int)
    for i in range(n):
        start=words[i][0]
        end=words[i][-1]
        a[start].append((end,words[i],i))
        out_deg[start]+=1
        in_deg[end]+=1
    flag=0
    m=len(in_deg)
    start=""
    end=""
    for i in a.keys():
        if(out_deg[i]-in_deg[i]==1):
            if(start==""):
                start=i
            else:
                flag=1
                break
        elif(in_deg[i]-out_deg[i]==1):
            if(end==""):
                end=i
            else:
                flag=1
                break
        elif(in_deg[i]!=out_deg[i]):
            flag=1
            break
    if(flag==1):
        print("***")
        continue
    if(start==""):
        start=min(a.keys())
    ans=[]
    vis=[0]*n
    def dfs(x):
        for i in range(len(a[x])):
            end,word,idx=a[x][i]
            if(vis[idx]==0):
                vis[idx]=1
                dfs(end)
                ans.append(word)
    dfs(start)
    if(len(ans)!=n):
        print("***")
    else:
        ans.reverse()
        print(".".join(ans))

```
## 4.其它算法
#### 1.字符串算法
**1.中心扩散法**
计算回文字串个数
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(2*n-1):
            l=i//2
            r=(i+1)//2
            while(l>=0 and r<n and s[l]==s[r]):
                l-=1
                r+=1
                ans+=1
        return ans
```
**2.KMP**
KMP.next[i]表示前i个数的最大公共前后缀的长度，也是在这一个位置失配时模式串的指针应该跳到的位置。  
构建next数组，目标串（模式串）指针在i=0，模式串指针在j=-1.同样可以使用KMP的移动规则，每次两个指针前移一位并记录next[i]，如果失配j就往回跳，一位都不对跳到-1自然从头开始。  
找循环节，最小循环节长度=L-next[L]。
```python
while(True):
    s=input()
    if(s=='.'):
        break
    n=len(s)
    next=[-1]*(n+1)
    i=0
    j=-1
    while(i<n):
        if(j==-1 or s[i]==s[j]):
            i+=1
            j+=1
            next[i]=j
        else:
            j=next[j]
    l=n-next[n]
    if(n%l==0):
        print(n//l)
    else:
        print(1)

```
**3.Shunting Yard调度场算法**
中序转后序
```python
n=int(input())
val={"+":1,"-":1,"*":2,"/":2}
for _ in range(n):
    s=input()
    num=""
    ans=[]
    sign=[]
    for i in s:
        if(i.isdigit() or i=='.'):
            num+=i
        else:
            if(num!=""):
                ans.append(num)
                num=""
            if(i=="("):
                sign.append(i)
            elif(i==')'):
                while(sign and sign[-1]!="("):
                    temp=sign[-1]
                    sign.pop()
                    ans.append(temp)
                sign.pop()
            elif(i in "+-*/"):
                while(sign and sign[-1] in "+-*/" and val[sign[-1]]>=val[i]):
                    temp=sign[-1]
                    sign.pop()
                    ans.append(temp)
                sign.append(i)
    if(num!=""):
        ans.append(num)
    while(sign):
        ans.append(sign.pop())
    print(" ".join(ans))

```
中序表达式求值：中序转后序+波兰表达式求值
```python
a=list(input().split())
s1=[]
s2=[]
dic={"+":1,"-":1,"*":2,"/":2}
def cal(x,y,t):
    x=float(x)
    y=float(y)
    if(t=="+"):
        return x+y
    elif(t=="-"):
        return x-y
    elif(t=="*"):
        return x*y
    elif(t=="/"):
        return x/y
    return 0
for i in a:
    if(i.isdigit()):
        s1.append(i)
    else:
        while(s2 and dic[i]<=dic[s2[-1]]):
            t=s2.pop()
            y=s1.pop()
            x=s1.pop()
            s1.append(cal(x,y,t))
        s2.append(i)
while(s2):
    y=s1.pop()
    x=s1.pop()
    t=s2.pop()
    s1.append(cal(x,y,t))
print(f"{float(s1[-1]):.2f}")
```
#### 2.计概补充
**1.数学**
数字华容道
求全排列序列的奇偶性，即求把它还原成1-n正序的交换次数。全排列可以唯一分解为多个循环。一个有 n 个数的循环可以通过 n-1 次元素交换变回递增的序列。
```python
T=int(input())
def cycle(a):
    m=len(a)
    vis=bytearray(m)
    ans=0
    for i in range(m):
        if(not vis[i]):
            res=0
            j=i
            while(not vis[j]):
                vis[j]=1
                j=a[j]-1
                res+=1
            ans=(ans+res-1)&1
    return ans
for _ in range(T):
    n=int(input())
    a=[]
    tmp=1
    for i in range(n):
        t=list(map(int,input().split()))
        if(0 in t):
            t.remove(0)
            if(n%2==0):
                tmp=i
        a.extend(t)
    if((cycle(a)+tmp)&1):
        print("yes")
    else:
        print("no")
```
exgcd:求ax+by=gcd(a,b)的解  
->ax=1(mod b)  
(ax+by=m有解->gcd(a,b)整除m)
```python
x=0
y=0
def exgcd(a,b):#ax+by=gcd(a,b)
    global x,y
    if(b==0):
        x=1
        y=0
        return
    exgcd(b,a%b)
    x,y=y,x-(a//b)*y
a,b=map(int,input().split())
exgcd(a,b)
print((x%b+b)%b)
```
**2.位运算**
位运算分治
颠倒二进制位
```python
m0 = 0x55555555  # 01010101 ...
m1 = 0x33333333  # 00110011 ...
m2 = 0x0f0f0f0f  # 00001111 ...
m3 = 0x00ff00ff  # 00000000111111110000000011111111
m4 = 0x0000ffff  # 00000000000000001111111111111111

class Solution:
    def reverseBits(self, n: int) -> int:
        n=(n>>1&m0)|((n&m0)<<1)
        n=(n>>2&m1)|((n&m1)<<2)
        n=(n>>4&m2)|((n&m2)<<4)
        n=(n>>8&m3)|((n&m3)<<8)
        n=(n>>16&m4)|((n&m4)<<16)
        return n
```
**3.滑动窗口+优先队列**
Flowerpot S
```python
from collections import deque
n,d=map(int,input().split())
rain=[]
for i in range(n):
    t=list(map(int,input().split()))
    rain.append(t)
rain=sorted(rain,key=lambda x:x[0])
maxq=deque()
minq=deque()
left=0
ans=float("INF")
for i in range(n):
    while(maxq and rain[maxq[-1]][1]<=rain[i][1]):
        maxq.pop()
    maxq.append(i)
    while(minq and rain[minq[-1]][1]>=rain[i][1]):
        minq.pop()
    minq.append(i)
    while(rain[maxq[0]][1]-rain[minq[0]][1]>=d and left<i):
        ans=min(ans,rain[i][0]-rain[left][0])
        if(maxq[0]==left):
            maxq.popleft()
        if(minq[0]==left):
            minq.popleft()
        left+=1
if(ans==float("INF")):
    print(-1)
else:
    print(ans)
```
**4.dp**
矩阵的最大非负积
```python
class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp_max=[[-1 for _ in range(n)]for _ in range(m)]
        dp_min=[[-1 for _ in range(n)]for _ in range(m)]
        dp_max[0][0]=grid[0][0]
        dp_min[0][0]=grid[0][0]
        for i in range(1,m):
            dp_min[i][0]=dp_min[i-1][0]*grid[i][0]
            dp_max[i][0]=dp_max[i-1][0]*grid[i][0]
        for i in range(1,n):
            dp_min[0][i]=dp_min[0][i-1]*grid[0][i]
            dp_max[0][i]=dp_max[0][i-1]*grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                dp_min[i][j]=min(dp_min[i-1][j]*grid[i][j],dp_max[i-1][j]*grid[i][j],dp_min[i][j-1]*grid[i][j],dp_max[i][j-1]*grid[i][j])
                dp_max[i][j]=max(dp_min[i-1][j]*grid[i][j],dp_max[i-1][j]*grid[i][j],dp_min[i][j-1]*grid[i][j],dp_max[i][j-1]*grid[i][j])
        t=dp_max[m-1][n-1]
        mod=10**9+7
        if(t<0):
            return -1
        else:
            return t%mod
print(Solution().maxProductPath([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]))
```
可以被机器人摧毁的最大墙壁数目
```python
from cmath import inf
from typing import List
from bisect import bisect_left,bisect_right
class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        a=[(0,0)]+sorted(zip(robots,distance),key=lambda x:x[0])+[(inf,0)]
        m=len(robots)
        n=len(walls)
        walls.sort()
        dp=[[0 for _ in range(2)] for _ in range(m+1)]#第i+1个机器人向左/右射击,前i个最大值
        for i in range(1,m+1):
            r=a[i][0]
            d=a[i][1]
            maxleft=max(r-d,a[i-1][0]+1)
            left=bisect_left(walls,maxleft)
            cur1=bisect_right(walls,r)
            cur2=bisect_left(walls,r)
            for j in range(2):
                if(j==0):
                    minright=min(r+d,a[i+1][0]-a[i+1][1]-1)
                else:
                    minright=min(r+d,a[i+1][0]-1)
                right=bisect_right(walls,minright)
                dp[i][j]=max(dp[i-1][0]+cur1-left,dp[i-1][1]+right-cur2)
        return max(dp[m][0],dp[m][1])

print(Solution().maxWalls([10,2],[5,1],[5,2,7]))
```
带通配符的字符串匹配
```python
from math import gcd
a=" "+input().strip()
b=" "+input().strip()
n=len(a)
m=len(b)
dp=[[0 for _ in range(m+1)]for _ in range(n+1)]#a的前i位与b的前j位能否匹配
dp[0][0]=1
for i in range(1,n):
    if(a[i]=="*"):
        dp[i][0]=dp[i-1][0]
    else:
        break
for i in range(1,n):
    if(a[i]=="*"):
        first=-1
        if(dp[i][0]):
            first=0
        else:
            for j in range(1,m):
                if(dp[i-1][j]):
                    first=j
                    break
        if(first!=-1):
            for j in range(first,m):
                dp[i][j]=1
    elif(a[i]=='?'):
        for j in range(1,m):
            dp[i][j]=dp[i-1][j-1]
    else:
        for j in range(1,m):
            dp[i][j]=dp[i-1][j-1] and a[i]==b[j]

def get_gcd(arr):
    res=arr[0]
    for i in range(1,len(arr)):
        res=gcd(res,arr[i])
    return res

if(dp[n-1][m-1]):
    print("matched")
    res=[0]*n
    i=n-1
    j=m-1
    while(i>0):
        if(a[i]=="*"):
            if(dp[i-1][j]):
                i-=1
            else:
                res[i]+=1
                j-=1
        else:
            res[i]+=1
            i-=1
            j-=1
    s=[]
    cur=0
    for i in range(1,n):
        if(a[i]=="*" or a[i]=='?'):
            if(i>1 and a[i]!=a[i-1] and cur>0):
                s.append(cur)
                cur=0
            cur+=res[i]
        else:
            if(cur>0):
                s.append(cur)
                cur=0
    if(cur>0):
        s.append(cur)
    if(len(s)==0):
        print(0)
    else:
        print(sum(s)//get_gcd(s))
else:
    print("not matched")
```
**5.dfs&bfs**
解数独
```python
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        row=[0]*9
        col=[0]*9
        block=[[0 for _ in range(3)]for _ in range(3)]
        spaces=[]
        def flip(i,j,digit):
            row[i]^=(1<<digit)
            col[j]^=(1<<digit)
            block[i//3][j//3]^=(1<<digit)
        def dfs(step):
            global valid
            if(step==len(spaces)):
                return True
            i,j=spaces[step]
            mask=(~(row[i]|col[j]|block[i//3][j//3]))&0x1ff
            while(mask):
                qaq=mask&(-mask)
                digit=bin(qaq).count('0')-1
                flip(i,j,digit)
                board[i][j]=str(digit+1)
                if(dfs(step+1)):
                    return True
                flip(i,j,digit)
                board[i][j]='.'
                mask&=(mask-1)
            return False

        for i in range(9):
            for j in range(9):
                if(board[i][j]!='.'):
                    flip(i,j,int(board[i][j])-1)
        while(True):
            flag=False
            for i in range(9):
                for j in range(9):
                    if(board[i][j]=='.'):
                        mask=(~(row[i]|col[j]|block[i//3][j//3]))&0x1ff
                        if(not (mask&(mask-1))):
                            digit=bin(mask).count('0')-1
                            flip(i,j,digit)
                            board[i][j]=str(digit+1)
                            flag=True
            if(not flag):
                break
        for i in range(9):
            for j in range(9):
                if(board[i][j]=='.'):
                    spaces.append((i,j))
        dfs(0)
```
求连通块长度
```python
m=int(input())
n=int(input())
a=[]
dx=[0,-1,0,1]
dy=[-1,0,1,0]
def dfs(x,y,step):
    area=1
    for i in range(4):
        if((a[x][y]&(1<<i))==0):
            xx=x+dx[i]
            yy=y+dy[i]
            if(0<=xx<m and 0<=yy<n and vis[xx][yy]==0):
                vis[xx][yy]=1
                area+=dfs(xx,yy,step+1)
    return area
for i in range(m):
    a.append(list(map(int,input().split())))
ans=0
max_res=0
vis=[[0 for _ in range(n)]for _ in range(m)]
for i in range(m):
    for j in range(n):
        if(vis[i][j]==0):
            vis[i][j]=1
            max_res=max(max_res,dfs(i,j,1))
            ans+=1
print(ans)
print(max_res)
```
通配符匹配-词梯
```python
from collections import deque,defaultdict
n=int(input())
words=[]
for i in range(n):
    words.append(input())
patterns=defaultdict(list)
for i in range(n):
    for j in range(4):
        p=words[i][:j]+"*"+words[i][j+1:]
        patterns[p].append(i)
start,end=input().split()
si=words.index(start)
ei=words.index(end)
q=deque()
q.append(si)
flag=0
pre=[-1]*n
vis=[0]*n
vis[si]=1
while(q):
    node=q.popleft()
    if(node==ei):
        flag=1
        break
    for i in range(4):
        w=words[node][:i]+"*"+words[node][i+1:]
        if(w in patterns):
            for j in patterns[w]:
                if(vis[j]==0):
                    vis[j]=1
                    pre[j]=node
                    q.append(j)
            patterns.pop(w)
if(flag==0):
    print("NO")
else:
    res=[]
    cur=ei
    while(cur!=-1):
        res.append(words[cur])
        cur=pre[cur]
    print(*res[::-1])

```
骑士周游：采用Warnsdorff's Rule进行启发式搜索。即在后续格子中选择出路最少、离边界最近的，可以减少后续走了很长的路然后进入死胡同的可能性。
```python
n=int(input())
x0,y0=map(int,input().split())
vis=[[0 for _ in range(n)]for _ in range(n)]
vis[x0][y0]=1
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[-1,-2,-2,-1,1,2,2,1]
flag=0
def get_degree(x,y):
    degree=0
    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n and vis[xx][yy]==0):
            degree+=1
    return degree
def get_dist(x,y):
    return (x-n/2.0)**2+(y-n/2.0)**2
def dfs(x,y,step):
    global flag
    if(step==n*n):
        flag=1
        return
    candidates=[]
    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n and vis[xx][yy]==0):
            candidates.append((get_degree(xx,yy),-get_dist(xx,yy),xx,yy))
    candidates.sort()
    for _,__,xx,yy in candidates:
        vis[xx][yy]=1
        dfs(xx,yy,step+1)
        if(flag==1):
            return
        vis[xx][yy]=0
dfs(x0,y0,1)
if(flag==1):
    print("success")
else:
    print("fail")
```
通过质数传送到达终点的最小跳跃次数：埃氏筛+bfs
```python
from collections import deque,defaultdict
from typing import List
from math import sqrt
MX=1000001
factors=[[] for _ in range(MX)]
for i in range(2,MX):
    if(not factors[i]):
        for j in range(i,MX,i):
            factors[j].append(i)
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n=len(nums)
        m=max(nums)
        groups=defaultdict(list)
        for i in range(n):
            for p in factors[nums[i]]:
                groups[p].append(i)
        q=deque()
        q.append((0,0))
        vis=[0]*n
        vis[0]=1
        while(q):
            idx,steps=q.popleft()
            if(idx==n-1):
                return steps
            cur=groups[nums[idx]]
            cur.append(idx+1)
            if(idx-1>=0):
                cur.append(idx-1)
            for i in cur:
                if(i!=idx and not vis[i]):
                    vis[i]=1
                    q.append((i,steps+1))
            cur.clear()
print(Solution().minJumps([1,2,4,6]))
```
小木棍
```python
#include<bits/stdc++.h>
using namespace std;
bool cmp(int a,int b){
    return a>b;
}
int a[70],vis[70],n;
bool dfs(int cnt,int rest,int last,int len){
    if(cnt==1) return true;
    if(rest==0) return dfs(cnt-1,len,0,len);
    int i=last,pre=-1;
    while(i<n){
        if(a[i]>rest){
            i=lower_bound(a,a+n,rest,cmp)-a;
            continue;
        }
        if(vis[i]){
            i++;
            continue;
        }
        if(a[i]==pre){
            i++;
            continue;
        }
        vis[i]=1;
        if(dfs(cnt,rest-a[i],i+1,len)) return true;
        vis[i]=0;
        pre=a[i];
        if(rest==len||rest==a[i]) return false;
        i++;
    }
    return false;
}
int main(){
    int sum=0;
    scanf("%d",&n);
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
        sum+=a[i];
    }
    sort(a,a+n,cmp);
    memset(vis,0,sizeof(vis));
    for(int i=a[0];i<=sum;i++){
        if(sum%i!=0) continue;
        if(dfs(sum/i,i,0,i)){
            printf("%d\n",i);
            break;
        }
    }
}
```
**6.单调栈**
完美交易窗口
```python
import bisect
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
maxs=[]
mins=[]
res=0
high=[0]*n
for i in range(n):
    while(maxs and a[maxs[-1]]<a[i]):#decrease
        maxs.pop()
    high[i]=maxs[-1] if maxs else -1
    maxs.append(i)
for i in range(n):
    while(mins and a[mins[-1]]>=a[i]):#increase
        mins.pop()
    t=bisect.bisect_right(mins,high[i])
    if(t<len(mins)):
        res=max(res,i-mins[t]+1)
    mins.append(i)
print(res)
```
**7.堆优化**
产生至少 K 个峰值的最少操作次数
由于峰值必须两两间隔，每个点到达峰值的操作数固定，题目转化为求k个不相邻数的最小值。  
1.dp[i][j]:0-i，j个不相邻数的最小值。同打家劫舍II.  
2.贪心+反悔。使用小根堆，每次取堆顶，并标记左右两边的数。将这个值更新为左右的值加和减去该值，重新放入堆中，并更新左右数的坐标。  
复杂度O(n)+O(klogn)=O(nlogn)
```python
import heapq
class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        if(n//2<k):
            return -1
        a=[0]*n
        for i in range(n):
            p=nums[i-1]
            q=nums[i]
            r=nums[(i+1)%n]           
            a[i]=max(0,max(p,r)+1-q)
        l=[0]*n
        r=[0]*n
        for i in range(n):
            l[i]=(i-1+n)%n
            r[i]=(i+1)%n
        q=[]
        heapq.heapify(q)
        for i in range(n):
            heapq.heappush(q,(a[i],i))
        vis=[0]*n
        ans=0
        cnt=0
        while(cnt<k):
            if(not q):
                return -1
            val,idx=heapq.heappop(q)
            if(vis[idx]):
                continue
            ans+=val
            vis[l[idx]]=1
            vis[r[idx]]=1
            a[idx]=a[l[idx]]+a[r[idx]]-val
            heapq.heappush(q,(a[idx],idx))
            l[idx]=l[l[idx]]
            r[idx]=r[r[idx]]
            l[r[idx]]=idx
            r[l[idx]]=idx
            cnt+=1
        return ans
```
n路归并（两数组求两两相加的最小n个数）
```python
import heapq
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    a=[]
    for i in range(m):
        t=list(map(int,input().split()))
        a.append(sorted(t))
    ans=a[0].copy()
    for k in range(1,m):
        minq=[]
        cur=[]
        for i in range(n):
            heapq.heappush(minq,(ans[i]+a[k][0],i,0))
        for i in range(n):
            sum,idx1,idx2=heapq.heappop(minq)
            cur.append(sum)
            if(idx2+1<n):
                heapq.heappush(minq,(ans[idx1]+a[k][idx2+1],idx1,idx2+1))
        ans=cur.copy()
    print(*ans)
```
**8.Shell排序**
插入排序：左边的数列有序，每次将右边的数一下一下往左边挪，直到找到合适的位置插入。 
希尔排序：将数列分为gap组，0-gap-1即为每组第一个元素，每次向左移动gap个位置，这样保证每组有序。  
gap由Hibbard增量序列生成，最后gap=1相当于插入排序。每次元素能跳得更多，保证效率。
```python
n=int(input())
a=list(map(int,input().split()))
h=[]
i=1
gap=1
while(gap<=n):
    h.append(gap)
    i+=1
    gap=(1<<i)-1
h.reverse()
for gap in h:
    for i in range(gap,n):
        temp=a[i]
        j=i
        while(j>=gap and a[j-gap]>temp):
            a[j]=a[j-gap]
            j-=gap
        a[j]=temp
    print(" ".join(map(str,a)))
```
## 5.特殊技巧
```python
from decimal import Decimal
a=Decimal(b)#保持精度

f"{a}output{b:.2f}" #f-string.保留两位小数

i=s.bit_length()#返回二进制的位数
i=s.bit_count()#返回二进制中1的个数

@cache
dfs(a,b,c):
	……
dfs.cache_clear()#缓存存储dfs状态的参数组合

global ans #寻找全局变量。  
nonlocal ans #寻找上一层函数的变量
```
