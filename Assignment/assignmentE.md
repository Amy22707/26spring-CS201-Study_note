# DSA Assignment E: 20260603期末机考

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

### E30646:缺失的第一个正数

http://cs101.openjudge.cn/practice/30646

思路：

从一开始搜索，注意整个数组都为负的情况，因此结束点取范围最大值即可。

代码：

```python
n=int(input())
a=list(map(int,input().split()))
s=set(a)
for i in range(1,2**31):
    if(i not in s):
        print(i)
        break
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_xLIqZBEfV)



### E30930:猫猫水群聊

 http://cs101.openjudge.cn/practice/30930


思路：

按倒序排序然后判断当前值是否比序号大即可。

代码：

```python
n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
ans=0
for i in range(n):
    if(a[i]>=i+1):
        ans=i+1
    else:
        break
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_qhbkzMnun)



### M30874:匹配队友

http://cs101.openjudge.cn/practice/30874

思路：

将每一组队友的编号存下来，最后判断是否成队。

代码：

```python
from collections import defaultdict
n=int(input())
a=list(input().split())
ans=[0]*n
res=[[0 for _ in range(3)]for _ in range(n+1)]
idx0=1
idx1=1
idx2=1
teams=defaultdict(list)
for i in range(n):
    s=a[i]
    if(s=='D'):
        if(res[idx0][0]>=3):
            idx0+=1
        res[idx0][0]+=1
        ans[i]=idx0
        teams[idx0].append(i)
    elif(s=='T'):
        if(res[idx1][1]>=1):
            idx1+=1
        res[idx1][1]+=1
        ans[i]=idx1
        teams[idx1].append(i)
    elif(s=='H'):
        if(res[idx2][2]>=1):
            idx2+=1
        res[idx2][2]+=1
        ans[i]=idx2
        teams[idx2].append(i)
t=max(ans)
for i in range(t,-1,-1):
    if(len(teams[i])<5):
        for j in teams[i]:
            ans[j]=0
    else:
        break
print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_hd4XEZf5V)



### M30680:森林局部排序遍历

http://cs101.openjudge.cn/practice/30680

思路：

离散化，找根，然后按照题目要求dfs.

代码：

```python
from collections import defaultdict
n=int(input())
g=defaultdict(list)
idx=defaultdict(int)#self->idx
tran=[]#idx->self
cnt=0
for i in range(n):
    temp=list(map(int,input().split()))
    head=temp[0]
    g[head]=temp[1:]
    idx[head]=cnt
    cnt+=1
    tran.append(head)
in_deg=[0]*n#idx
for i in g.keys():
    for j in g[i]:
        in_deg[idx[j]]+=1
par=[]#self
for i in range(n):
    if(in_deg[i]==0):
        par.append(tran[i])
par.sort()
# vis=[0]*n
def dfs(x,fa):
    if(len(g[x])==0):
        print(x)
        return
    elif(x==fa):
        print(x)
        return
    else:
        qaq=[x]
        for i in g[x]:
            qaq.append(i)
        qaq.sort()
        for i in qaq:
            dfs(i,x)
for i in par:
    dfs(i,-10086)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_jAL3WAsnQ)


### M30947:Ask for Likes

http://cs101.openjudge.cn/practice/30947

思路：

对每个询问进行约数分解。然后依次搜索每个数换成某个比它大的因数之后能不能达到目标。
剪枝：1.由于$2^{30}>{10}^9$,因此如果大于1的数的个数多于30个，那么肯定不能达到目标。因此实际进入dfs的候选数不超过30个。
2.后缀积数组，如果剩余的数小于当前后缀积，那么乘起来肯定大了，可以剪掉。
3.使用lru_cache进行记忆化搜索。

代码

```python
import sys
from math import sqrt
from bisect import bisect_left
from functools import lru_cache
n,q=map(int,input().split())
c=list(map(int,input().split()))
cnt=0
for i in range(n):
    if(c[i]==0):
        c[i]=1
    if(c[i]>1):
        cnt+=1
c.sort(reverse=True)
if(cnt>30):
    for i in range(q):
        x=int(input())
        print("No")
    sys.exit(0)
suf=[1]*(n+1)
for i in range(n-1,-1,-1):
    suf[i]=suf[i+1]*c[i]
for i in range(q):
    x=int(input())
    div=[]
    for j in range(1,int(sqrt(x))+1):
        if(x%j==0):
            div.append(j)
            if(j*j!=x):
                div.append(x//j)
    div.sort()
    @lru_cache(None)    
    def dfs(i,rem):
        global cnt
        if(i==cnt):
            return (rem==1 or n-cnt>0)
        if(suf[i]>rem):
            return False
        for d in div:
            if(d>rem):
                break
            if(d>=c[i] and rem%d==0):
                if(dfs(i+1,rem//d)):
                    return True
        return False
    dfs.cache_clear()
    if(dfs(0,x)):
        print("Yes")
    else:
        print("No")

```



<mark>（至少包含有"Accepted"）</mark>

![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_us6ZnkAWd)



### T30913:猫猫逛公园 

http://cs101.openjudge.cn/practice/30913

思路：

使用Tarjan进行SCC缩点，然后遍历所有边，建立DAG并将属于同一SCC的边归类。然后对每个SCC中的边作数学处理，得到SCC内部的最大愉悦值。再在拓扑序上dp，注意起点给定，因此除了起点之外的点的dp值设为-1，dp的更新基于前一点已被更新，即大于零。

代码

```python
import sys
from math import sqrt,ceil
from collections import deque
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
g=[[]for _ in range(n+1)]
for i in range(m):
    x,y,w=map(int,input().split())
    g[x].append((y,w))
start=int(input())
dfn=[0]*(n+1)
low=[0]*(n+1)
time=0
s=[]
scc=[]
in_s=[0]*(n+1)
idx=[0]*(n+1)
def tarjan(k):
    global time
    time+=1
    low[k]=dfn[k]=time
    s.append(k)
    in_s[k]=1
    for i,qaq in g[k]:
        if(dfn[i]==0):
            tarjan(i)
            low[k]=min(low[k],low[i])
        elif(in_s[i]):
            low[k]=min(low[k],dfn[i])
    if(low[k]==dfn[k]):
        tmp=[]
        while(True):
            x=s.pop()
            tmp.append(x)
            idx[x]=len(scc)
            in_s[x]=0
            if(x==k):
                break
        scc.append(tmp)
for i in range(1,n+1):
    if(dfn[i]==0):
        tarjan(i)
lens=len(scc)
in_deg=[0]*lens
vis=set()
dag=[[]for _ in range(lens)]
sums=[[] for _ in range(lens)]
for i in range(1,n+1):
    for j,qaq in g[i]:
        if(idx[i]!=idx[j]):
            in_deg[idx[j]]+=1
            dag[idx[i]].append((idx[j],qaq))
        else:
            sums[idx[i]].append(qaq)
res=[]
for i in range(lens):
    cnt=0
    for j in sums[i]:
        k=ceil((sqrt(8*j+1)-1)/2)
        val=k*j-(k-1)*k*(k+1)//6
        cnt+=val
    res.append(cnt)
q=deque()
dp=[-1]*lens
sidx=idx[start]
dp[sidx]=res[sidx]
for i in range(lens):
    if(in_deg[i]==0):
        q.append(i)
while(q):
    node=q.popleft()
    for i,val in dag[node]:
        if(dp[node]!=-1):
            dp[i]=max(dp[i],dp[node]+res[i]+val)
        in_deg[i]-=1
        if(in_deg[i]==0):
            q.append(i)
print(int(max(dp)))
```



<mark>（至少包含有"Accepted"）</mark>

![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_GgvRM1JKp)


### U30919:猫猫去旅行 

http://cs101.openjudge.cn/practice/30919

思路：

双堆动态维护中位数。

代码

```python

```



<mark>（至少包含有"Accepted"）</mark>





## 2. 课程总结

如果愿意，请同学或多或少做一个本门课程的学习总结。便于之后师弟师妹跟进学习，也便于教师和助教改进教学。例如：分享自己的学习心得、笔记。

期末机考AC4，最后一题在细节处理上尚缺，一直WA没有调出来。T5的剪枝在AI的辅助下才明白。
本学期由于专业课较多，在数算上的练习量较上学期少了一些，总练习量为200+。月考（周考）参与了大部分，一般AC5-6题。虽然期末考试有点遗憾，但在数算课中学到了相当多的数据结构和编程技巧，也非常感谢闫老师与助教老师们一学期的辛苦付出。
本学期的资料与代码已同步上传至[Github](https://github.com/Amy22707/26spring-CS201-Study_note),大作业部分的md文件后续会更新。