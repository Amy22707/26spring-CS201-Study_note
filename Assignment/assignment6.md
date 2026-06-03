# DSA Assignment #6: 🌲（1/3）

*Updated 2026-04-05 21:54 GMT+8*
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

### E94.二叉树的中序遍历

dfs, stack, https://leetcode.cn/problems/binary-tree-inorder-traversal/

思路：

递归/迭代

代码：

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
print(Solution().inorderTraversal(TreeNode(1,None,TreeNode(2,TreeNode(3)))))
```

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

print(Solution().inorderTraversal(TreeNode(1,None,TreeNode(2,TreeNode(3)))))
```


代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_Svjc8It1f)



### E108.将有序数组转换为二叉搜索树

https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/


思路：

每次令中间节点为根节点，最终一定符合要求。递归分治解决。

代码：

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
print(Solution().sortedArrayToBST([-10,-3,0,5,9]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_jGlaMqo3F)




### M102.二叉树的层序遍历

bfs, https://leetcode.cn/problems/binary-tree-level-order-traversal/

思路：

bfs，每一次把当前层所有点都处理完。

代码：

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

print(Solution().levelOrder(TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_xo_FqC_zJ)



### M1123.最深叶节点的最近公共祖先

dfs, https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves/

思路：

递归。如果左子树深度大于右子树，那么lca是左子树的lca。如果深度相等，最深节点分布在两边，lca标记为当前节点。

代码：

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
print(Solution().lcaDeepestLeaves(TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_F70tXloGw)



### M07161: 森林的带度数层次序列存储

tree, http://cs101.openjudge.cn/practice/07161/

思路：

解析层次遍历同样使用队列，构建树之后再后序遍历输出即可。

代码

```python
from collections import deque
class TreeNode:
    def __init__(self,x,):
        self.val=x
        self.children=[]
def postorder(root):
    if(root is None):
        return []
    for child in root.children:
        postorder(child)
    res.append(root.val)
    return res
n=int(input())
ans=[]
for qaq in range(n):
    s=list(input().split())
    t=len(s)
    t//=2
    nodes=[]
    deg=[]
    for qwq in range(t):
        nodes.append(s[qwq*2])
        deg.append(int(s[qwq*2+1]))
    q=deque()
    root=TreeNode(nodes[0])
    degree0=deg[0]
    q.append((root,degree0))
    cur=0
    while(q):
        n=len(q)
        for i in range(n):
            node,degree=q.popleft()
            for j in range(cur+1,cur+degree+1):
                child=TreeNode(nodes[j])
                node.children.append(child)
                q.append((child,deg[j]))
            cur+=degree
    res=[]
    ans.extend(postorder(root))
print(" ".join(ans))


```



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_gD98JMVZM)



### M27928: 遍历树

 adjacency list, dfs, http://cs101.openjudge.cn/practice/27928/

思路：

使用邻接表存树。对树dfs，每次将当前节点与子节点排序，并依次dfs。如果轮到了当前节点就输出。

代码

```python
def dfs(node):
    temp=[node]
    for i in adj[node]:
        temp.append(i)
    temp.sort()
    for i in temp:
        if(i==node):
            print(i)
        else:
            dfs(i)
n=int(input())
adj={}
all_nodes=set()
children_nodes=set()
for i in range(n):
    temp=list(map(int,input().split()))
    val=temp[0]
    adj[val]=temp[1:]
    all_nodes.add(val)
    for j in temp[1:]:
        children_nodes.add(j)
root=list(all_nodes-children_nodes)[0]
dfs(root)
```



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_1NTdCLAKd)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

学习了树的基础操作，包括建树、遍历等。
清明那周由于身体原因没怎么写题，本周补了十多道程设的题目，以及AI课的MNIST作业，数算这边练习较少，希望下周可以把每日选做补了。



