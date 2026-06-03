# Assignment #1: OOP

*Updated 2026-03-03 11:25 GMT+8*
 *Compiled by <mark>生命科学学院 薛之瑶</mark> (2026 Spring)*



**作业的各项评分细则及对应的得分**

| 标准                  | 等级                                                                       | 得分  |
| ------------------- | ------------------------------------------------------------------------ | --- |
| 按时提交                | 完全按时提交：1分<br/>提交有请假说明：0.5分<br/>未提交：0分                                    | 1 分 |
| 源码、耗时（可选）、解题思路（可选）  | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于2个：0分              | 1 分 |
| AC代码截图              | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于：0分                | 1 分 |
| 清晰头像、PDF文件、MD/DOC附件 | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
| 学习总结和个人收获           | 提交了学习总结和个人收获：1分<br/>未提交学习总结或内容不详：0分                                      | 1 分 |
| 总得分： 5              | 总分满分：5分                                                                  |     |
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

### E27653: Fraction类

OOP, http://cs101.openjudge.cn/pctbook/E27653/

> 主要是练习面向对象编程写法，这样力扣题目，笔试都没有问题了。机考时候，不是必须OOP，能AC就可以。
>

思路：
目标类需要实现最简化和分数加法。
注意分母为一，负数和分子等于零的情况。加法函数和输出函数可使用特殊方法函数名。


代码：

```python
def gcd(a,b):
    a=abs(a)
    b=abs(b)
    if(a<b):
        a,b=b,a
    while(a%b!=0):
        c=a%b
        a=b
        b=c
    return b
class Fraction:
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        self.denominator=denominator
        self.simplify()
    def simplify(self):
        a=self.numerator
        b=self.denominator
        if(a==0):
            self.numerator=0
            self.denominator=1
            return
        c=gcd(a,b)
        self.numerator=a//c
        self.denominator=b//c
    def __add__(self,other):
        a,b,c,d=self.numerator,self.denominator,other.numerator,other.denominator
        e=a*d+b*c
        f=b*d
        return Fraction(e,f)
    def __str__(self):
        a=self.numerator
        b=self.denominator
        if(b==1):
            return f"{a}"
        return f"{a}/{b}"
a,b,c,d=map(int,input().split())
x=Fraction(a,b)
y=Fraction(c,d)
print(x+y)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_ko1M_U4mL)


### E190.颠倒二进制位

bit manipulation, https://leetcode.cn/problems/reverse-bits/


思路：

位运算分治。颠倒的方法是将二进制位分成两半，各自颠倒再交换顺序。而每一半可以继续这样下去，直到只剩两位。因此考虑分治，通过位运算可以位数相同的操作同时进行。

代码：

```python
m0 = 0x55555555  # 01010101 ...
m1 = 0x33333333  # 00110011 ...
m2 = 0x0f0f0f0f  # 00001111 ...
m3 = 0x00ff00ff  # 00000000111111110000000011111111
m4 = 0x0000ffff  # 00000000000000001111111111111111

class Solution:
    def reverseBits(self, n: int) -> int:
        n=(n>>1&m0)|((n&m0)<<1)
        n=(n>>2&m1)|((n&m1)<<2)
        n=(n>>4&m2)|((n&m2)<<4)
        n=(n>>8&m3)|((n&m3)<<8)
        n=(n>>16&m4)|((n&m4)<<16)
        return n
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_WTxb4htC6)



### E1356.根据数字二进制下 1 的数目排序

bit manipulation, https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/

思路：

可以使用递推方法计算1的数目。根据最后一位建立递推关系，然后自定义排序即可。

代码：

```cpp
class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        vector<int> bit(10001,0);
        for(int i=1;i<=10000;i++){
            bit[i]=bit[i>>1]+(i&1);
        }
        sort(arr.begin(),arr.end(),[&](int x,int y){
            if(bit[x]<bit[y]) return true;
            if(bit[x]>bit[y]) return false;
            return x<y;
        });
        return arr;
    }
};
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_YWg4gfTyZ)



### M27300: 模型整理

sortings, AI, http://cs101.openjudge.cn/pctbook/M27300/



思路：

将参数量转成整型并比较，输出的时候再还原回去即可。使用Decimal以保持精度。

代码：

```python
from collections import defaultdict
from decimal import Decimal
n=int(input())
models=defaultdict(list)
for i in range(n):
    a,b=input().split('-')
    if(b[-1]=='M'):
        c=Decimal(b[0:-1])*1000000
    elif(b[-1]=='B'):
        c=Decimal(b[0:-1])*1000000000
    models[a].append(c)
ans=dict(sorted(models.items(),key=lambda x:x[0]))
for k in ans:
    ans[k].sort()
    tmp=[]
    for i in ans[k]:
        if(i>=1000000 and i<1000000000):
            s=str(i/1000000)
            tmp.append(s+"M")
        else:
            s=str(i/1000000000)
            tmp.append(s+"B")
    print(f"{k}: {', '.join(tmp)}")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_hWKtZCVjt)



### M1536.排布二进制网格的最少交换次数

greedy, matrix, https://leetcode.cn/problems/minimum-swaps-to-arrange-a-binary-grid/



思路：

由于越往下需要满足的条件越宽松，因此对每行向下遍历，遇到符合条件的就交换上去。

代码：

```python
class Solution:
    def minSwaps(self, grid: list[list[int]]) -> int:
        n=len(grid)
        zeroes=[n]*n
        for i in range(n):
            for j in range(n-1,-1,-1):
                if(grid[i][j]==1):
                    zeroes[i]=n-1-j
                    break
        ans=0
        for i in range(n):
            qaq=n-1-i
            flag=0
            for j in range(i,n):
                if(zeroes[j]>=qaq):
                    flag=1
                    ans+=(j-i)
                    zeroes[i+1:j+1]=zeroes[i:j]
                    break
            if(flag==0):
                return -1
        return ans
print(Solution().minSwaps([[0,0,1],[1,1,0],[1,0,0]]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_n1DESK46Q)


### T20052:最大点数（同2048规则）

dfs, matrices, http://cs101.openjudge.cn/pctbook/T20052/

思路：

直接搜索即可。
模拟的时候注意不要更改原数组，数据量较低使用deepcopy即可。先把所有数字移到一边（移动零），再合并，再移动零。

代码：

```python
from copy import deepcopy
m,n,p=map(int,input().split())
def left(b):
    a=deepcopy(b)
    global m,n
    for i in range(m):
        cur=0
        for j in range(n):
            if(a[i][j]!=0):
                a[i][cur],a[i][j]=a[i][j],a[i][cur]
                cur+=1
        for j in range(n):
            if(a[i][j]!=0 and j!=n-1 and a[i][j]==a[i][j+1]):
                a[i][j]*=2
                a[i][j+1]=0
        cur=0
        for j in range(n):
            if(a[i][j]!=0):
                a[i][cur],a[i][j]=a[i][j],a[i][cur]
                cur+=1
    return a
def right(b):
    a=deepcopy(b)
    global m,n
    for i in range(m):
        cur=n-1
        for j in range(n-1,-1,-1):
            if(a[i][j]!=0):
                a[i][cur],a[i][j]=a[i][j],a[i][cur]
                cur-=1
        for j in range(n-1,-1,-1):
            if(a[i][j]!=0 and j!=0 and a[i][j]==a[i][j-1]):
                a[i][j]*=2
                a[i][j-1]=0
        cur=n-1
        for j in range(n-1,-1,-1):
            if(a[i][j]!=0):
                a[i][cur],a[i][j]=a[i][j],a[i][cur]
                cur-=1
    return a
def up(b):
    a=deepcopy(b)
    global m,n
    for j in range(n):
        cur=0
        for i in range(m):
            if(a[i][j]!=0):
                a[cur][j],a[i][j]=a[i][j],a[cur][j]
                cur+=1
        for i in range(m):
            if(a[i][j]!=0 and i!=m-1 and a[i][j]==a[i+1][j]):
                a[i][j]*=2
                a[i+1][j]=0
        cur=0
        for i in range(m):
            if(a[i][j]!=0):
                a[cur][j],a[i][j]=a[i][j],a[cur][j]
                cur+=1
    return a
def down(b):
    a=deepcopy(b)
    global m,n
    for j in range(n):
        cur=m-1
        for i in range(m-1,-1,-1):
            if(a[i][j]!=0):
                a[cur][j],a[i][j]=a[i][j],a[cur][j]
                cur-=1   
        for i in range(m-1,-1,-1):
            if(a[i][j]!=0 and i!=0 and a[i][j]==a[i-1][j]):
                a[i][j]*=2
                a[i-1][j]=0
        cur=m-1
        for i in range(m-1,-1,-1):
            if(a[i][j]!=0):
                a[cur][j],a[i][j]=a[i][j],a[cur][j]
                cur-=1   
    return a    
def dfs(a,step):
    global ans,m,n,p
    # print("TEST",step)
    # for i in range(m):
    #     for j in range(n):
    #         print(a[i][j],end=' ')
    #     print()
    if(step==p):
        res=0
        for i in range(m):
            for j in range(n):
                res=max(res,a[i][j])
        ans=max(ans,res)
        return
    dfs(left(a),step+1)
    dfs(right(a),step+1)
    dfs(up(a),step+1)
    dfs(down(a),step+1)
    return
a=[]
ans=0
for i in range(m):
    t=list(map(int,input().split()))
    a.append(t)
dfs(a,0)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_11LIARKqX)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

学习了位运算分治等位运算技巧，以及OOP的一些写法。
同步完成每日选做。
寒假完成了力扣热题100中除链表、二叉树外的全部题目，第一周补了十道链表题。

