# DSA Assignment #A: 5月份月考

*Updated 2026-05-06 15:43 GMT+8*
 *Compiled by <mark>生命科学学院 薛之瑶</mark> (2026 Spring)*



>**说明：**
>
>1. **解题与记录：**
>
>     对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E04137: 最小新整数 

monotonic stack, http://cs101.openjudge.cn/practice/04137/

思路：

单调栈。

代码：

```python
t=int(input())
for _ in range(t):
    n,k=input().split()
    k=int(k)
    m=len(n)
    s=[]
    cnt=0
    for c in n:
        while(s and c<s[-1] and cnt<k):
            s.pop()
            cnt+=1
        s.append(c)
    while(cnt<k):
        s.pop()
        cnt+=1
    print("".join(s))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_Ph1Culng7)


### E04143: 和为给定数 

two pointers, http://cs101.openjudge.cn/dsapre/04143/


思路：

排序后双指针。

代码：

```python
n=int(input())
a=list(map(int,input().split()))
m=int(input())
a.sort()
i=0
j=n-1
flag=0
while(i<j):
    if(a[i]+a[j]==m):
        flag=1
        print(a[i],a[j])
        break
    elif(a[i]+a[j]>m):
        j-=1
    else:
        i+=1
if(flag==0):
    print("No")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_fsk_p_9PU)


### M27638: 求二叉树的高度和叶子数目

http://cs101.openjudge.cn/practice/27638/

思路：

先用节点和叶子节点的差集找根，然后dfs即可。

代码：

```python
n=int(input())
tree=[]
child=set()
leaves=0
for i in range(n):
    x,y=map(int,input().split())
    tree.append([x,y])
    child.add(x)
    child.add(y)
    if(x==-1 and y==-1):
        leaves+=1
for i in range(n):
    if(i not in child):
        root=i
        break
dep=0
def dfs(node,parent,cur):
    global dep
    if(tree[node][0]==-1 and tree[node][1]==-1):
        dep=max(dep,cur)
        return
    for i in tree[node]:
        if(i!=parent and i!=-1):
            dfs(i,node,cur+1)
dfs(root,-1,0)
print(dep,leaves)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_KLkr93_ZD)



### M30720: 败方树的构建与维护

http://cs101.openjudge.cn/practice/30720/

思路：

对每个节点，存储败者与胜者信息，以便继续比较。从叶子往上bfs构建败方树，修改同理。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_ee5QB4Fql)



### 27093: 排队又来了

Segment Tree, Discretization（离散化）, binary search, http://cs101.openjudge.cn/practice/27093/

思路：
如果i<j，且$|h_i-h_j|$>k，则$h_i$与$h_j$的位置不能互换。因此将$h_i$->$h_j$连边，所得即为DAG.根据规则，输出最小拓扑排序即可。
考虑优化复杂度，求每个点入度时，排序并离散化，在从左往右扫描的过程中使用树状数组维护已经扫描过的高度情况。拓扑排序使用线段树优化区间修改入度，即采用线段树记录最小值，每次取根节点并二分查找需要更新入度的区间。

代码

```python
import heapq
from bisect import bisect_left,bisect_right
n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
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
for c in res:
    print(c)
```



<mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_W7zeMLzNh)


### T30669: 地铁换乘

LCA, binary lifting, http://cs101.openjudge.cn/practice/30669/

思路：

倍增lca以得到两节点之间的距离，然后计算出相遇点即可。

代码

```python
from math import log2
n,t=map(int,input().split())
tree=[[] for _ in range(n+1)]
for i in range(n-1):
    x,y=map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)
p,q,v1,v2=map(int,input().split())
max_log=20
par=[0]*(n+1)
dep=[0]*(n+1)
def dfs(node,parent,depth):
    par[node]=parent
    dep[node]=depth
    for i in tree[node]:
        if(i!=parent):
            dfs(i,node,depth+1)
    return
dfs(t,0,0)
up=[[0 for _ in range(max_log)]for _ in range(n+1)]
for i in range(1,n+1):
    up[i][0]=par[i]
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
    return par[x]
def get(x,k):
    for i in range(max_log):
        if((k>>i)&1):
            x=up[x][i]
    return x
lca_node=lca(p,q)
d1=dep[p]-dep[lca_node]
d2=dep[q]-dep[lca_node]
tot=(d1+d2)//(v1+v2)
s1=tot*v1
ans=0
if(s1<=d1):
    ans=get(p,s1)
else:
    ans=get(q,d1+d2-s1)
print(tot,dep[ans])
```



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_iHFFGvcl8)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

月考AC4.两道M题都是模拟，求二叉树深度用dfs，败方树bfs更新。排队即为拓扑排序，考虑用BIT计算入度并用线段树动态更新。地铁换乘即为LCA问题。

