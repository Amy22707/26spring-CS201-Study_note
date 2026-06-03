# DSA Assignment #9: 图（1/3）

*Updated 2026-04-28 13:47 GMT+8*
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

### M28046: 词梯

bfs, http://cs101.openjudge.cn/practice/28046/

思路：

使用通配符模式匹配为节点连边。bfs时直接在通配符桶中寻找邻居。剪枝：搜过一个桶之后，可以直接把这个桶删除，因为已经中转过了，不需要再用到。

代码：

```python
from collections import deque,defaultdict
n=int(input())
words=[]
for i in range(n):
    words.append(input())
patterns=defaultdict(list)
for i in range(n):
    for j in range(4):
        p=words[i][:j]+"*"+words[i][j+1:]
        patterns[p].append(i)
start,end=input().split()
si=words.index(start)
ei=words.index(end)
q=deque()
q.append(si)
flag=0
pre=[-1]*n
vis=[0]*n
vis[si]=1
while(q):
    node=q.popleft()
    if(node==ei):
        flag=1
        break
    for i in range(4):
        w=words[node][:i]+"*"+words[node][i+1:]
        if(w in patterns):
            for j in patterns[w]:
                if(vis[j]==0):
                    vis[j]=1
                    pre[j]=node
                    q.append(j)
            patterns.pop(w)
if(flag==0):
    print("NO")
else:
    res=[]
    cur=ei
    while(cur!=-1):
        res.append(words[cur])
        cur=pre[cur]
    print(*res[::-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_hs27mrcDB)



### M433.最小基因变化

bfs, https://leetcode.cn/problems/minimum-genetic-mutation/


思路：

bfs.

代码：

```python
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        g=['A','T','C','G']
        q=deque()
        q.append((0,startGene))
        vis=set()
        vis.add(startGene)
        if(endGene not in bank):
            return -1
        flag=0
        while(q):
            l,s=q.popleft()
            if(s==endGene):
                flag=1
                return l
            for i in range(8):
                for j in range(4):
                    ng=s[:i]+g[j]+s[i+1:]
                    if(ng not in bank or ng in vis):
                        continue
                    q.append((l+1,ng))
                    vis.add(ng)
        if(flag==0):
            return -1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_fy1l4rknx)


### sy382: 有向图判环 中等

Karn, dfs, Floyd-Warshall, https://sunnywhy.com/sfbj/10/3/382

思路：

有向图判环，需使用三状态标记，判断下一个节点是否在当前路径上。（有可能出现访问了已经访问但不在当前路径上的节点的情况。）
无向图判环，排除是否为父节点即可。

代码：

```python
n,m=map(int,input().split())
a=[[] for _ in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    a[u].append(v)
vis=[0]*n
flag=0
def dfs(node):
    global flag
    for c in a[node]:
        if(vis[c]==0):
            vis[c]=2
            dfs(c)
        elif(vis[c]==2):
            flag=1
            return
        vis[c]=1
for i in range(n):
    if(vis[i]==0):
        vis[i]=2
        dfs(i)
        vis[i]=1
    if(flag==1):
        break
if(flag==1):
    print("Yes")
else:
    print("No")

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_rs6Zb0J9Y)



### M909.蛇梯棋

bfs, https://leetcode.cn/problems/snakes-and-ladders/

思路：

bfs模拟即可。

代码：

```python
from collections import deque
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n=len(board)
        a=[[0 for _ in range(n)]for _ in range(n)]
        x=n-1
        y=0
        dir=1
        idx=[(-1,-1)]
        for i in range(1,n*n+1):
            a[x][y]=i
            idx.append((x,y))
            if(dir==1):
                y=y+1
                if(y==n):
                    y=n-1
                    x=x-1
                    dir=-1
            elif(dir==-1):
                y=y-1
                if(y==-1):
                    y=0
                    x=x-1
                    dir=1
        q=deque()
        vis=[float("inf")]*(n*n+1)
        q.append((0,1))
        flag=0
        while(q):
            l,cur=q.popleft()
            if(cur==n*n):
                flag=1
                return l
            for i in range(1,7):
                t=cur+i
                if(t>n*n):
                    continue
                x1,y1=idx[t]
                if(board[x1][y1]!=-1):
                    t=board[x1][y1]
                if(t<=n*n and vis[t]>l+1):
                    vis[t]=l+1
                    q.append((l+1,t))
        if(flag==0):
            return -1

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_9WId8OcO1)



### M28050: 骑士周游

dfs, http://cs101.openjudge.cn/practice/28050/

思路：

采用Warnsdorff's Rule进行启发式搜索。即在后续格子中选择出路最少、离边界最近的，可以减少进入死胡同的可能性。

代码

```python
n=int(input())
x0,y0=map(int,input().split())
vis=[[0 for _ in range(n)]for _ in range(n)]
vis[x0][y0]=1
dx=[-2,-1,1,2,2,1,-1,-2]
dy=[-1,-2,-2,-1,1,2,2,1]
flag=0
def get_degree(x,y):
    degree=0
    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n and vis[xx][yy]==0):
            degree+=1
    return degree
def get_dist(x,y):
    return (x-n/2.0)**2+(y-n/2.0)**2
def dfs(x,y,step):
    global flag
    if(step==n*n):
        flag=1
        return
    candidates=[]
    for i in range(8):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n and vis[xx][yy]==0):
            candidates.append((get_degree(xx,yy),-get_dist(xx,yy),xx,yy))
    candidates.sort()
    for _,__,xx,yy in candidates:
        vis[xx][yy]=1
        dfs(xx,yy,step+1)
        if(flag==1):
            return
        vis[xx][yy]=0
dfs(x0,y0,1)
if(flag==1):
    print("success")
else:
    print("fail")
```



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_3cPLfm5jn)



### T37.解数独

backtracking, hash table, https://leetcode.cn/problems/sudoku-solver/

思路：

启发式搜索：先把能唯一确定的格子填好，再对不确定的格子dfs.
使用二进制存储每行、列与九宫格的状态。每次使用lowbit操作取出最低位的1并依次尝试。

代码

```python
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        row=[0]*9
        col=[0]*9
        block=[[0 for _ in range(3)]for _ in range(3)]
        spaces=[]
        def flip(i,j,digit):
            row[i]^=(1<<digit)
            col[j]^=(1<<digit)
            block[i//3][j//3]^=(1<<digit)
        def dfs(step):
            global valid
            if(step==len(spaces)):
                return True
            i,j=spaces[step]
            mask=(~(row[i]|col[j]|block[i//3][j//3]))&0x1ff
            while(mask):
                qaq=mask&(-mask)
                digit=bin(qaq).count('0')-1
                flip(i,j,digit)
                board[i][j]=str(digit+1)
                if(dfs(step+1)):
                    return True
                flip(i,j,digit)
                board[i][j]='.'
                mask&=(mask-1)
            return False

        for i in range(9):
            for j in range(9):
                if(board[i][j]!='.'):
                    flip(i,j,int(board[i][j])-1)
        while(True):
            flag=False
            for i in range(9):
                for j in range(9):
                    if(board[i][j]=='.'):
                        mask=(~(row[i]|col[j]|block[i//3][j//3]))&0x1ff
                        if(not (mask&(mask-1))):
                            digit=bin(mask).count('0')-1
                            flip(i,j,digit)
                            board[i][j]=str(digit+1)
                            flag=True
            if(not flag):
                break
        for i in range(9):
            for j in range(9):
                if(board[i][j]=='.'):
                    spaces.append((i,j))
        dfs(0)
        """
        Do not return anything, modify board in-place instead.
        """
board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
for i in range(9):
    for j in range(9):
        print(board[i][j],end=" ")
    print()
```



<mark>（至少包含有"Accepted"）</mark>



![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_Fka1iiQmC)


## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这周作业主要复习了搜索，骑士周游和解数独学习了启发式搜索的思路。词梯的通配符匹配和剪枝优化都很有意思，学到了新的优化方法。



