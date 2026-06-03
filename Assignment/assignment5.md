# DSA Assignment #5: 20260401 cs201 Mock Exam

*Updated 2026-04-01 15:20 GMT+8*
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

### E02039: 反反复复	

matrix, http://cs101.openjudge.cn/practice/02039/

思路：

直接模拟即可。

代码：

```python
n=int(input())
a=list(input())
a.insert(0," ")
for i in range(1,n+1):
    for j in range(1,len(a)):
        if(j%(2*n)==i or j%(2*n)==(2*n+1-i if i!=1 else 0)):
            print(a[j],end="")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_m_ENVuOny)



### E02092: Grandpa is Famous	

implementation, http://cs101.openjudge.cn/practice/02092/


思路：

字典存储，扫两边记下最大值和第二大值即可。

代码：

```python
from collections import defaultdict
while(True):
    n,m=map(int,input().split())
    if(n==0 and m==0):
        break
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    rank=defaultdict(int)
    for i in range(n):
        for j in range(m):
            rank[a[i][j]]+=1
    maxm=max(rank.values())
    res=0
    for i in rank.values():
        if(i>res and i<maxm):
            res=i
    ans=[]
    for i in rank.keys():
        if(rank[i]==res):
            ans.append(i)
    print(" ".join(map(str,sorted(ans))))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_W-WVitdW0)



### M02774: 木材加工	

binary search, http://cs101.openjudge.cn/practice/02774/

思路：

二分答案。

代码：

```python
n,k=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
if(sum(a)<k):
    print(0)
else:
    ans=0
    l=1
    r=max(a)
    while(l<=r):
        mid=(l+r)>>1
        cnt=0
        for i in a:
            cnt+=i//mid
        if(cnt>=k):
            ans=max(ans,mid)
            l=mid+1
        else:
            r=mid-1
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_jzwvn5_y9)




### M04077: 出栈序列统计

dp, dfs, math, http://cs101.openjudge.cn/practice/04077/

思路：

卡特兰数。

代码：

```python
from math import comb
n=int(input())
print(comb(2*n,n)//(n+1))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_zGXK6rbKP)



### M30637: 合法出栈序列pub

stack, http://cs101.openjudge.cn/practice/M30637/

思路：

直接模拟即可。

代码

```python
x=input()
n=len(x)
while(True):
    try:
        s=input()
        t=[]
        i=0#s
        j=0#x
        if(len(s)!=n):
            print("NO")
            continue
        while(j<n):
            if(len(t)>0 and s[i]==t[-1]):
                t.pop()
                i+=1
            else:
                t.append(x[j])
                j+=1
        while(i<n):
            if(len(t)>0 and s[i]==t[-1]):
                t.pop()
                i+=1
            else:
                break
        if(len(t)==0):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
```



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_yKRj9R_f1)



### T30102:完美交易窗口

monotonic stack, http://cs101.openjudge.cn/practice/T30102/

思路：

一个单调减栈maxs记录j左侧第一个比它大的元素（即所有可能买入点的左边界），另一个单调增栈mins记录j左侧所有可能的买入点（即从它开始到j始终保持它是序列最小值）。因此更新mins的过程中可以直接二分找到对于每个右边界，最长的左边界。
月考时候没多想直接得出左侧第一个比它大的与右侧第一个比它小的然后暴力枚举了，怎么不算一种$n^2$过百万（）（虽然期望复杂度是$O(nlogn)$)。

代码

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



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_dgMts85D5)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

月考总体比较顺利，T6调了一会，一个半小时AK了。
继续完成每日选做。严肃进行OOP练习和魔兽世界中。