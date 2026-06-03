# DSA Assignment #4: 线性结构

*Updated 2026-03-23 22:22 GMT+8*
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

### E160.相交链表

hash table, linked list, two pointers, https://leetcode.cn/problems/intersection-of-two-linked-lists/

思路：

双指针。两个指针分别指向两个链表的头部，遍历完一个则指向另一个开头。若两个链表相交，则最终会在交叉点相遇。若不相交，则最后到达对方的终点，返回Null.

代码：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_6RULcTts9)



### E206.反转链表

recursion, linked list, https://leetcode.cn/problems/reverse-linked-list/


思路：

当前节点与其指向的节点之间的指针要反转，此时第三个节点会失去被指索引。因此同时记1，2，3三个指针，2指向1，2变成1，3变成2.

代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_5Sn05I56f)



### M234.回文链表

linked list, two pointers, https://leetcode.cn/problems/palindrome-linked-list/

<mark>请用快慢指针实现</mark> `O(1)` 空间复杂度。

思路：

使用快慢指针，快指针速度为2，慢指针速度为1，从而找到链表中点。然后把后半部分反转，再两个指针同时走判断是否回文。

代码：

```python
class Solution:
    def reverseList(head):
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while(fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
        head2=Solution.reverseList(slow)
        head1=head
        if(head1.val!=head2.val):
            return False
        while(head1.next!=None and head2.next!=None):
            head1=head1.next
            head2=head2.next
            if(head1.val!=head2.val):
                return False
        return True
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_aCWoUUoA1)



### M24591:中序表达式转后序表达式

stack, http://cs101.openjudge.cn/practice/24591/

思路：

Shunting Yard算法。建立答案栈和符号栈，根据运算规则存入弹出符号。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_ebyL18pU-)



### M146.LRU缓存

hash table, doubly-linked list, https://leetcode.cn/problems/lru-cache/

思路：

要求查找和插入都O(1)，使用哈希表。要求灵活将内容移到队尾与删除队首，使用双向链表。
也可以使用Python内置的ordered_dict完成，有move_to_end()和popitem(last=False)模块。

代码

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


<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_UXzvQQOuO)



### P2698 [USACO12MAR] Flowerpot S

monotonic queue, https://www.luogu.com.cn/problem/P2698

思路：

滑动窗口+单调队列。把所有点按x坐标排序，易知右侧点的left必定比左侧点的left大。因此可以使用滑动窗口，同时使用两个单调队列分别维护段中的最大值与最小值，每次的新值加入队尾并保持递增/递减，最值从队头取，老值从队头删除。

代码

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



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_elA25TeYh)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>
LRU缓存学习了ordered_dict以及双向链表的操作。Flowerpot S复习了滑窗的单调队列写法。
同步完成每日一题。解数独那道dfs很有意思，学习了相关位运算操作及启发式搜索的思想。




