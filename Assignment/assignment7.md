# DSA Assignment #7: 🌲（2/3）

*Updated 2026-04-09 15:45 GMT+8*
 *Compiled by <mark>同学的姓名、院系</mark> (2026 Spring)*



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

### M297.二叉树的序列化与反序列化

dfs, bfs, https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/

思路：

使用层次遍历进行序列化与反序列化。当子节点为空时，记为null，可以唯一确定树的序列。反序列化使用指针指向当前节点的左儿子，无论是否为空每次移动两格，可以证明能够还原二叉树。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_v5sQ8rdL9)



### M129.求根节点到叶节点数字之和

dfs, https://leetcode.cn/problems/sum-root-to-leaf-numbers/


思路：

dfs.

代码：

```python
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node,sum):
            if(node==None):
                return 0
            sum=sum*10+node.val
            if(node.left==None and node.right==None):
                return sum
            return dfs(node.left,sum)+dfs(node.right,sum)
        return dfs(root,0)
print(Solution().sumNumbers(TreeNode(1,TreeNode(2),TreeNode(3))))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_TcOtbpK-T)


### M22158:根据二叉树前中序序列建树

tree, http://cs101.openjudge.cn/practice/22158/



思路：

递归完成。先由先序遍历找到根，然后由根确定左子树和右子树，并进一步递归求解。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_UEOqgd5NE)



### M24729:括号嵌套树

dfs, stack, http://cs101.openjudge.cn/practice/24729/



思路：

括号匹配+前后序遍历

代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_GXr7x8Z7-)



### M01577: Falling Leaves

tree, http://cs101.openjudge.cn/practice/01577/



思路：

从根节点开始，将每一层的数依次插入BST中。插入的方法可以递归解决。

代码

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



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_ojH9L6ErE)



### 1843D. Apple Tree

 Combinatorics, dfs and similar, dp, math, trees, 1200,  https://codeforces.com/problemset/problem/1843/D

思路：

即求每个节点对应的叶子节点个数。dfs求解即可，注意用邻接表存树需判断是父节点还是子节点。

代码

```python
import sys
sys.setrecursionlimit(10**6)
t=int(input())
def dfs(parent,x):
    if(len(a[x])==1 and a[x][0]==parent):
        ans[x]=1
    for i in a[x]:
        if(i!=parent):
            dfs(x,i)
            ans[x]+=ans[i]

for _ in range(t):
    n=int(input())
    a=[[]for _ in range(n+1)]
    ans=[0 for _ in range(n+1)]
    for i in range(n-1):
        u,v=map(int,input().split())
        a[u].append(v)
        a[v].append(u)
    q=int(input())
    dfs(0,1)
    for i in range(q):
        u,v=map(int,input().split())
        print(ans[u]*ans[v])
```



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_NRG66s6TA)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

学习了二叉树层次遍历以序列化与反序列化的方法，以及通过前序与中序确定后序。巩固了dfs搜树的方法。
补了一周的每日选做。学习了Shell排序、ST表解决RMQ问题、dfn与倍增法求lca、堆优化的贪心+反悔算法等。

