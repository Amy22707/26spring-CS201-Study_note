# Assignment #3: 20260311 cs201 Mock Exam

*Updated 2026-03-11 15:24 GMT+8*
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

### E20742:泰波拿契數

implementation, http://cs101.openjudge.cn/practice/20742/

思路：

递推。

代码：

```python
n=int(input())
a=[0,1,1]
for i in range(3,n+1):
    a.append(a[i-1]+a[i-2]+a[i-3])
print(a[n])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_k0LcVYIdE)



### E30571.十进制整数的反码

bit manipulation, http://cs101.openjudge.cn/practice/E30571/


思路：

考场上换成字符串直接操作的。位运算解法考虑bit_length()取位数并将原数与全1二进制数按位异或，并特殊处理0的情况。

代码：

```python
n=int(input())
t=bin(n)[2:]
ans=""
for i in range(len(t)):
    if(t[i]=='0'):
        ans+='1'
    else:
        ans+='0'
print(int(ans,2))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_bPBzIZDNO)



### E29950:稳定的符文序列

two pointers, http://cs101.openjudge.cn/practice/E29950



思路：

滑动窗口。

代码：

```python
s=input()
n=len(s)
a=[0]*26
left=0
ans=0
cur=0
for i in range(n):
    a[ord(s[i])-ord('a')]+=1
    cur+=1
    while(a[ord(s[i])-ord('a')]>1):
        a[ord(s[left])-ord('a')]-=1
        cur-=1
        left+=1
    ans=max(ans,cur)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_vfpq-fMur)



### M30218:狭路相逢

stack, http://cs101.openjudge.cn/practice/M30218/



思路：

用栈模拟。易知幸存的怪物一定在栈底，每次遇到怪兽的时候不断弹出栈顶勇士即可。

代码：

```python
from collections import deque
n=int(input())
a=list(map(int,input().split()))
s=deque()
for i in range(n):
    if(a[i]>0):
        s.append(a[i])
    else:
        tmp=-a[i]
        while(s):
            t=s[-1]
            if(t<0):
                break
            s.pop()
            if(t>tmp):
                t-=tmp
                s.append(t)
                tmp=0
                break
            else:
                tmp-=t
        if(tmp>0):
            s.append(-tmp)
print(len(s))
print(" ".join(map(str,s)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_ZKosQpRi_)



### M02299: Ultra-QuickSort

merge sort, http://cs101.openjudge.cn/practice/02299/

思路：

归并排序求逆序对。

代码：

```python
ans=0
def merge(l,r):
    global ans
    if(l==r):
        return
    mid=(l+r)>>1
    merge(l,mid)
    merge(mid+1,r)
    i=l
    j=mid+1
    cur=l
    while(i<=mid and j<=r):
        if(a[i]>a[j]):
            ans+=(mid-i+1)
            a_new[cur]=a[j]
            cur+=1
            j+=1
        else:
            a_new[cur]=a[i]
            cur+=1
            i+=1
    while(i<=mid):
        a_new[cur]=a[i]
        cur+=1
        i+=1
    while(j<=r):
        a_new[cur]=a[j]
        cur+=1
        j+=1
    a[l:r+1]=a_new[l:r+1]
while(True):
    n=int(input())
    if(n==0):
        break
    a=[]
    ans=0
    a_new=[0]*n
    for i in range(n):
        t=int(input())
        a.append(t)
    merge(0,n-1)
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_NagBDhZek)



### M29954:逃离紫罗兰监狱

bfs, http://cs101.openjudge.cn/practice/29954 

思路：

多维bfs。新开一维记录使用技能的方法。

代码：

```python
from collections import deque
r,c,k=map(int,input().split())
a=[]
for i in range(r):
    t=input()
    a.append(t)
for i in range(r):
    for j in range(c):
        if(a[i][j]=='S'):
            x0=i
            y0=j
        elif(a[i][j]=='E'):
            x1=i
            y1=j
q=deque()
vis=[[[0 for _ in range(k+1)]for _ in range(c)]for _ in range(r)]
q.append([x0,y0,0,0])
vis[x0][y0][0]=1
dx=[0,1,0,-1]
dy=[1,0,-1,0]
flag=0
while(q):
    x,y,cur,l=q.popleft()
    if(flag==1):
        break
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<r and yy>=0 and yy<r):
            if(a[xx][yy]=='.'):
                if(vis[xx][yy][cur]==0):
                    vis[xx][yy][cur]=1
                    q.append([xx,yy,cur,l+1])
            elif(a[xx][yy]=='#'):
                if(cur<k and vis[xx][yy][cur+1]==0):
                    vis[xx][yy][cur+1]=1
                    q.append([xx,yy,cur+1,l+1])
            elif(a[xx][yy]=='E'):
                flag=1
                print(l+1)
                break
if(flag==0):
    print(-1)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_-S-eNPIHB)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

月考一开始做得比较急，被T2和T6都卡了一下。最后一个小时多一点AK了。
同步完成每日选做，做了几道程设的OOP题目。
这学期课程较多，刚开学几周没有多做很多题，后面适应节奏后再多练练。