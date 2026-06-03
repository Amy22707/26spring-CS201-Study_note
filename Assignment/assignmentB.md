# DSA Assignment #B: 20260513模拟考

*Updated 2026-05-13 13:35 GMT+8*
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

### E02724: 生日相同

sortings, http://cs101.openjudge.cn/pctbook/E02724/

思路：

使用defaultdict并排序。

代码：

```python
from collections import defaultdict
n=int(input())
a=defaultdict(list)
for i in range(n):
    idx,m,d=input().split()
    birth=int(m)*100+int(d)
    a[birth].append(idx)
a=dict(list(sorted(a.items(),key=lambda x:x[0])))
for i in a.keys():
    if(len(a[i])>1):
        mon=i//100
        day=i-mon*100
        print(mon,day,*a[i])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_2LH9bi9l9)



### E19963: 买学区房

math, http://cs101.openjudge.cn/practice/19963


思路：

使用statistics中median模块可直接求中位数。

代码：

```python
import statistics
n=int(input())
pairs=[i[1:-1] for i in input().split()]
distances=[sum(map(int,i.split(',')))for i in pairs]
cost=list(map(int,input().split()))
ave=[distances[i]/cost[i] for i in range(n)]
am=statistics.median(ave)
cm=statistics.median(cost)
ans=0
for i in range(n):
    if(ave[i]>am and cost[i]<cm):
        ans+=1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_d4nudsE0M)


### M20746: 满足合法工时的最少人数

binary search, http://cs101.openjudge.cn/practice/20746/

思路：

二分答案。

代码：

```python
from math import ceil
a=list(map(int,input().split(",")))
t=int(input())
l=1
r=max(a)
ans=r
while(l<=r):
    mid=(l+r)>>1
    s=0
    for i in a:
        s+=ceil(i/mid)
    if(s<=t):
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy__SFWseR3p)



### M07734: 虫子的生活

DSU, http://cs101.openjudge.cn/practice/07734/

思路：

使用种类并查集。开2n空间记录虫子的性别，如果遇到同一个性别的虫子连接在一起那么就矛盾。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_ibLXxPtTO)


### M02186: Popular Cows

SCC, http://cs101.openjudge.cn/practice/02186/

思路：

使用Tarjan缩点，一个SCC中的所有奶牛都相互爱慕。然后记录每个SCC的出度，可知如果有一个SCC的出度为0那么其中的所有点为最受欢迎，如果有多个SCC出度为0那么没有最受欢迎的奶牛。

代码

```python
import sys
sys.setrecursionlimit(1000000)
n,m=map(int,input().split())
c=[[]for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    c[x].append(y)
low=[0]*(n+1)
dfn=[0]*(n+1)
time=0
s=[]
scc=[]
idx=[0]*(n+1)
def tarjan(k):
    global time
    time+=1
    low[k]=dfn[k]=time
    s.append(k)
    for i in c[k]:
        if(dfn[i]==0):
            tarjan(i)
            low[k]=min(low[k],low[i])
        elif i in s:
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
cnt=len(scc)
out=[0]*cnt
for i in range(1,n+1):
    for j in c[i]:
        if(idx[i]!=idx[j]):
            out[idx[i]]+=1
ans=0
flag=0
for i in range(cnt):
    if(out[i]==0 and ans!=0):
        flag=1
        print(0)
        break
    elif(out[i]==0):
        ans+=len(scc[i])
if(flag==0):
    print(ans)
```



<mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy__kcE67hta)


### T01236: Network of Schools 238

SCC, http://cs101.openjudge.cn/practice/01236/

思路：

使用Tarjan缩点。第一问即求入度为0的点个数，因为这些点没有学校传给它们。第二问特判整个图是否强连通，如果强连通则输出0，否则答案为入度和出度为0的点的个数中的较大值。（第二问要求使整个图强连通最少要增加的边，考虑将入度0和出度0的点两两连接。）

代码

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



<mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_Jg7-q4Ilu)


## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次题目是赛后补的，前面四道题难度尚可，虫子的生活除了种类并查集之外还了解了带权并查集和dfs染色的思路。后两道题学习了Tarjan SCC缩点。



