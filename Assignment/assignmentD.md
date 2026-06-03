# DSA Assignment D: 20260527模拟考

*Updated 2026-05-20 16:47 GMT+8*
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

### M27351:01最小生成树

补图的连通分量, http://cs101.openjudge.cn/practice/27351

思路：

要求最小生成树即需要包含尽可能多的零边。考虑零边连接成的连通块，最终的MST即为将这些连通块连在一起，因此MST的大小即为连通块个数减1.使用bfs+差集操作避免超时。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_FyxVR5Dt8)



### M30910:邮递员送快递

正向/反向图 Dijkstra, http://cs101.openjudge.cn/practice/30910


思路：

构建正向与反向图，并分别跑一遍Dijkstra。注意如果使用邻接矩阵存图要判重，以及此处要使用邻接表以避免超时。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_24ZBVqURe)



### M30912:累加树

构建 BST + 右-根-左累加 + BFS 输出, http://cs101.openjudge.cn/practice/30912

思路：

插入构建BST，然后从大到小，即右根左遍历，全局变量累加和并更新到节点中。最后bfs层序遍历输出。

代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_NFEAGVNlN)



### M30899:火星大工程

关键路径, http://cs101.openjudge.cn/practice/30899

思路：

求关键路径以及关键活动。根据入度和出度进行正向和反向拓扑排序，以此更新节点最早开始时间和最晚开始时间。关键路径长度即为所有节点最早开始时间的最大值。对于每条边，如果起点的最早开始时间加工程长度等于终点的最晚开始时间，那么它是关键活动，开始时间必须确定。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_ISnnBgkjd)



### T30868:upstairs

同余最短路, http://cs101.openjudge.cn/practice/30868

思路：

同余最短路。选择a,b,c中最小的数（不妨a）作为最后叠加的层数，问题转化为在模a意义下，h=by+cz，而当此时的h最小，它是否小于目标的h。因此对每个余数u构建(u+b) mod a和(u+c) mod a的路径，从0开始跑一遍Dijkstra，得到的即为最小的h.

代码

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



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_-yybvXID5)



### T30921:猫猫搭积木

并查集, http://cs101.openjudge.cn/practice/30921

思路：

按秩合并并查集，同时维护代表节点的集合中的所有元素。注意计算集合个数的操作需要特判自己与自己合并的情况，因此在merge函数中进行。

代码

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



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_6ZNSDzXpQ)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

本次模拟考学到了很多新东西，如0-1最小生成树的连通块缩点、关键路径、同余最短路等。
Leetcode热题100之前剩了几道二叉树和链表没写，今天补完了。
![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_VuE9A93-o)

