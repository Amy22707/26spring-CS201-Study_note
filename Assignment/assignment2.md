# Assignment #2: 位运算、前缀和、树状数组、归并排序 & 状态压缩

*Updated 2026-03-10 11:00 GMT+8*
 *Compiled by <mark>生命科学学院 薛之瑶</mark> (2026 Spring)*



**作业的各项评分细则及对应的得分**

| 标准                                 | 等级                                                         | 得分 |
| ------------------------------------ | ------------------------------------------------------------ | ---- |
| 按时提交                             | 完全按时提交：1分<br/>提交有请假说明：0.5分<br/>未提交：0分  | 1 分 |
| 源码、耗时（可选）、解题思路（可选） | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于2个：0分 | 1 分 |
| AC代码截图                           | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于：0分 | 1 分 |
| 清晰头像、PDF文件、MD/DOC附件        | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
| 学习总结和个人收获                   | 提交了学习总结和个人收获：1分<br/>未提交学习总结或内容不详：0分 | 1 分 |
| 总得分： 5                           | 总分满分：5分                                                |      |
>
>
>
>**说明：**
>
>1. **解题与记录：**
>
>      对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. **课程平台：**课程网站位于Canvas平台（https://pku.instructure.com ）。该平台将在<mark>第2周</mark>选课结束后正式启用。在平台启用前，请先完成作业并将作业妥善保存。待Canvas平台激活后，再上传你的作业。
>
>3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E868.二进制间距

bit manipulation, https://leetcode.cn/problems/binary-gap/

> 主要是练习面向对象编程写法，这样力扣题目，笔试都没有问题了。机考时候，不是必须OOP，能AC就可以。
>

思路：

直接模拟即可。

代码：

```python
class Solution:
    def binaryGap(self, n: int) -> int:
        ans=0
        cnt=1
        flag=0
        while(n):
            if(flag==1 and n&1==0):
                cnt+=1
            elif(n&1==1):
                if(flag==0):
                    flag=1
                else:
                    ans=max(ans,cnt)
                    cnt=1
            n>>=1
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_d25Wmsaq_)



### M304.二维区域和检索 - 矩阵不可变

prefix sum, https://leetcode.cn/problems/range-sum-query-2d-immutable/


思路：

二维前缀和。左边多留一行一列。

代码：

```python
class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        m=len(matrix)
        n=len(matrix[0])
        sum=[[0 for _ in range(n+1)]for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                sum[i+1][j+1]=sum[i+1][j]+sum[i][j+1]+matrix[i][j]-sum[i][j]
        self.sum=sum
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum[row2+1][col2+1]-self.sum[row2+1][col1]-self.sum[row1][col2+1]+self.sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
obj=NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(obj.sumRegion(2, 1, 4, 3))
print(obj.sumRegion(1, 1, 2, 2))
print(obj.sumRegion(1, 2, 2, 4))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_tJ4xH0MvM)



### M1680.连接连续二进制数字

bit manipulation, https://leetcode.cn/problems/concatenation-of-consecutive-binary-numbers/



思路：

直接模拟。连接的方法是先左移再按位与。

代码：

```python
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans=0
        mod=1000000007
        for i in range(1,n+1):
            t=i.bit_length()
            ans=(ans<<t)|i
            ans%=mod
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_MziCpnh6E)



### M1461.检查一个字符串是否包含所有长度为 K 的二进制子串

bit manipulation, https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/



思路：

位运算滑动窗口。哈希表存长度为k的二进制数的大小，每次移动一位存入。

代码：

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n=len(s)
        st=set()
        if(k>n):
            return False
        num=int(s[:k],2)
        st.add(num)
        for i in range(k,n):
            num=(num-(int(s[i-k])<<(k-1)))*2+int(s[i])
            st.add(num)
        return len(st)==(1<<k)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_g-KuJ0F-T)


### M30178:数字华容道（Easy Version）

merge sort, binary indexed tree, http://cs101.openjudge.cn/practice/30178/

思路：

左右移动不改变序列奇偶性，上下移动相当于移动(n-1)位，如果n为偶数影响奇偶性，n为奇数则不影响。
因此转化为求整条序列的逆序对。这里采用树状数组。
先把所有数离散化为1-n(这道题不需要)，然后从后往前遍历。对当前元素x，答案加上tree[x-1]（即在此之前遇到过的小于x的数），然后在tree的x对应位置+1，表示已经遇到过了。

代码：

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_ewtw6QSsc)



### T30201: 旅行售货商问题

bitmask dp, http://cs101.openjudge.cn/practice/30201/

思路：

状压dp。每个点用一个二进制位表示状态，dp数组表示从起点到j号点，某状态下的最小代价。状态转移方程即每个点走或不走中的最小值。

代码：

```python
n=int(input())
a=[]
for i in range(n):
    t=list(map(int,input().split()))
    a.append(t)
dp=[[float("inf") for _ in range(n)]for _ in range(1<<n)]#从起点到j号点，状态为i时的最短路
dp[1][0]=0
for i in range(1<<n):
    if(i&1==0):
        continue
    for j in range(n):
        if((1<<j)&i)==0:
            for k in range(n):
                if((1<<k)&i):
                    dp[i|(1<<j)][j]=min(dp[i|(1<<j)][j],dp[i][k]+a[k][j])
minm=float("inf")
for i in range(n):
    minm=min(minm,dp[(1<<n)-1][i]+a[i][0])
print(minm)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_qQC6Ue_Ny)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

数字华容道学习了树状数组求逆序对的方法。同时学习了Hard版本的数学方法。
同步完成每日选做。学习了树形dp。



