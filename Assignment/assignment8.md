# DSA Assignment #8: 🌲（3/3）

*Updated 2026-04-21 19:09 GMT+8*
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

### M晴问9.7: 向下调整构建大顶堆

手搓堆, https://sunnywhy.com/sfbj/9/7

思路：

对二叉树的每个非叶节点，使其下沉到正确的位置，并递归调整受影响的子树。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_SiDUvkogpL)


### M1722.执行交换操作后的最小汉明距离

dsu, https://leetcode.cn/problems/minimize-hamming-distance-after-swap-operations/


思路：

并查集。同一个联通分量里面元素可以互相交换，因此比较每个分量的source和target即可。使用Counter统计个数，并贪心匹配。

代码：

```python
from typing import List
from collections import defaultdict,Counter
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n=len(source)
        m=len(allowedSwaps)
        fa=[i for i in range(n)]
        size=[1]*n
        def find(x):
            if(fa[x]!=x):
                fa[x]=find(fa[x])
            return fa[x]
        def merge(x,y):
            fx=find(x)
            fy=find(y)
            if(fx==fy):
                return
            if(size[fx]<size[fy]):
                fx,fy=fy,fx
            fa[fy]=fx
            size[fx]+=size[fy]
        for i in range(m):
            merge(allowedSwaps[i][0],allowedSwaps[i][1])
        d=defaultdict(list)
        for i in range(n):
            d[find(i)].append(i)
        ans=0
        for lst in d.values():
            cnt=Counter(source[i] for i in lst)
            for i in lst:
                if(cnt[target[i]]>0):
                    cnt[target[i]]-=1
                else:
                    ans+=1
        return ans

print(Solution().minimumHammingDistance([1,2,3,4], [2,1,4,5], [[0,1],[2,3]]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_uJowWf2tZ)



### T22161: 哈夫曼编码树

greedy, http://cs101.openjudge.cn/practice/22161/

思路：

自定义比较顺序。建树使用小根堆，每次取出最小两个作为左右节点，再把它们的父节点放回去。编码直接dfs即可。解码字符串根据搜索得出的表来，解码01串则直接在树上往下搜，搜到底记录答案并返回根部即可。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_-yxeZDXjP)


### M晴问9.5: 平衡二叉树的建立

手搓AVL, https://sunnywhy.com/sfbj/9/5/359

思路：

保持平衡的方法是左旋/右旋。根据高度差判断四种不平衡的情况，并对子树和根节点旋转。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_G_snPStyY)


### M208.实现Trie（前缀树）

trie, https://leetcode.cn/problems/implement-trie-prefix-tree/

思路：

26叉树。每个节点指向当前字母对应的子节点。

代码

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



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_IJ4AQtoeq)



### M307.区域和检索 - 数组可修改

segment tree, https://leetcode.cn/problems/range-sum-query-mutable/

思路：

单点修改+区间查询，使用树状数组/线段树。
树状数组：1-i的前缀和每次按lowbit(i)的长度拆分。
线段树：每个节点不断平分区间和

代码

树状数组：
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

线段树：
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

    def sums(self,node,start,end,l,r):
        if(l<=start and end<=r):
            return self.tree[node]
        if(end<l or start>r):
            return 0
        mid=(start+end)>>1
        return self.sums(node*2,start,mid,l,r)+self.sums(node*2+1,mid+1,end,l,r)
    
    def sumRange(self, left: int, right: int) -> int:
        return self.sums(1,0,self.n-1,left,right)
```


<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_OK2ssHIDH)


附：带lazy tag的线段树实现（区间修改+区间查询）
lazy tag即先存下要修改的地方，等访问到了再修改，且能够实现区间完全覆盖时就统一更新。
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

## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

作业布置的题目除了并查集之外都之前没有怎么练习过，全部手写了一遍，对其中的原理更加熟悉了。
期中周较忙，无额外练习题目。


