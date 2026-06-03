# DSA Assignment 520: 20260520模拟考

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

### E04080: Huffman编码树

http://cs101.openjudge.cn/practice/04080/

思路：

贪心地可知，Huffman编码的方式可使题目所求式子最小。

代码：

```python
import heapq
n=int(input())
a=list(map(int,input().split()))
q=[]
for i in a:
    heapq.heappush(q,i)
ans=0
while(len(q)>1):
    x=heapq.heappop(q)
    y=heapq.heappop(q)
    ans+=x+y
    heapq.heappush(q,x+y)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_0k09tufzV)



### M05443: 兔子与樱花

dijkstra, Floyd-Warshall, http://cs101.openjudge.cn/practice/05443/


思路：

使用Floyd求出全图最短路。记录路径的方法是对每一组起点和终点，记录起点下一步的点，并在松弛操作时更新。

代码：

```python
from collections import defaultdict
from math import inf
p=int(input())
d=defaultdict(int)
name=[]
for i in range(p):
    s=input()
    d[s]=i
    name.append(s)
a=[[inf for _ in range(p)]for _ in range(p)]
q=int(input())
next=[[0 for _ in range(p)]for _ in range(p)]
for i in range(q):
    x,y,z=input().split()
    idxx=d[x]
    idxy=d[y]
    a[idxx][idxy]=min(a[idxx][idxy], int(z))
    a[idxy][idxx]=min(a[idxy][idxx], int(z))
for i in range(p):
    for j in range(p):
        if(i!=j and a[i][j]!=inf):
            next[i][j]=j
        else:
            next[i][j]=-1
for k in range(p):
    for i in range(p):
        for j in range(p):
            if(a[i][k]+a[k][j]<a[i][j]):
                a[i][j]=a[i][k]+a[k][j]
                next[i][j]=next[i][k]
r=int(input())
for i in range(r):
    x,y=input().split()
    idxx=d[x]
    idxy=d[y]
    cur=idxx
    nxt=next[idxx][idxy]
    while(cur!=idxy):
        print(f"{name[cur]}->({a[cur][nxt]})->",end="")
        cur=nxt
        nxt=next[cur][idxy]
    print(name[idxy])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_ZgosGq_6J)



### M20741: 两座孤岛最短距离

bfs, http://cs101.openjudge.cn/practice/20741/

思路：

dfs求连通块找到一个孤岛，并从这个岛上每个点对另一个岛bfs找最短路。

代码：

```python
from collections import deque
n=int(input())
a=[]
vis=[[0 for _ in range(n)]for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
q=deque()
def dfs(x,y):
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n):
            if(vis[xx][yy]==0 and a[xx][yy]=="1"):
                vis[xx][yy]=1
                q.append((xx,yy,0))
                dfs(xx,yy)

for i in range(n):
    a.append(list(input()))
flag=0
for i in range(n):
    if(flag==1):
        break
    for j in range(n):
        if(a[i][j]=="1"):
            vis[i][j]=1
            q.append((i,j,0))
            dfs(i,j)
            flag=1
            break
for i in range(n):
    for j in range(n):
        if(vis[i][j]==1):
            a[i][j]='0'
while(q):
    x,y,dis=q.popleft()
    if(a[x][y]=="1"):
        print(dis-1)
        break
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if(xx>=0 and xx<n and yy>=0 and yy<n):
            if(vis[xx][yy]==0):
                vis[xx][yy]=1
                q.append((xx,yy,dis+1))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_Zo2cQfJg2)



### M24637: 宝藏二叉树

dp, dfs http://cs101.openjudge.cn/practice/24637/

思路：

树形dp.两个dp数组分别记录以i为根，选/不选i时整棵子树的最大值。从下往上更新。

代码：

```python
n=int(input())
a=[0]+list(map(int,input().split()))
dp1=[0 for _ in range(n+1)]#以i为根，选i
dp2=[0 for _ in range(n+1)]#以i为根，不选i
for i in range(n,0,-1):
    left=i<<1
    right=(i<<1)|1
    dp1[i]=a[i]
    if(left<=n):
        dp1[i]+=dp2[left]
        dp2[i]+=max(dp1[left],dp2[left])
    if(right<=n):
        dp1[i]+=dp2[right]
        dp2[i]+=max(dp1[right],dp2[right])
print(max(dp1[1],dp2[1]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_hATcmoMHG)



### T02337: Catenyms

Eulerian Path, http://cs101.openjudge.cn/practice/02337/

思路：

对每个单词建立从第一个字母指向最后一个字母的有向边，题目转化为求欧拉路径。通过入度与出度判断是否存在合法的路径以及起点，然后使用Hierholzer算法，dfs搜索，每次经过一条边即删除，并在当前点无出边时将该点倒序加入答案路径。

代码

```python
from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
t=int(input())
for _ in range(t):
    n=int(input())
    words=[]
    for i in range(n):
        tmp=input()
        words.append(tmp)
    words.sort()
    a=defaultdict(list)
    in_deg=defaultdict(int)
    out_deg=defaultdict(int)
    for i in range(n):
        start=words[i][0]
        end=words[i][-1]
        a[start].append((end,words[i],i))
        out_deg[start]+=1
        in_deg[end]+=1
    flag=0
    m=len(in_deg)
    start=""
    end=""
    for i in a.keys():
        if(out_deg[i]-in_deg[i]==1):
            if(start==""):
                start=i
            else:
                flag=1
                break
        elif(in_deg[i]-out_deg[i]==1):
            if(end==""):
                end=i
            else:
                flag=1
                break
        elif(in_deg[i]!=out_deg[i]):
            flag=1
            break
    if(flag==1):
        print("***")
        continue
    if(start==""):
        start=min(a.keys())
    ans=[]
    vis=[0]*n
    def dfs(x):
        for i in range(len(a[x])):
            end,word,idx=a[x][i]
            if(vis[idx]==0):
                vis[idx]=1
                dfs(end)
                ans.append(word)
    dfs(start)
    if(len(ans)!=n):
        print("***")
    else:
        ans.reverse()
        print(".".join(ans))
```



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_E8BwzE9Qh)



### T30878:力场叠加模拟

segment tree, lazy propagation, http://cs101.openjudge.cn/practice/30878/

思路：

使用lazy tag的线段树。

代码

```python
class SegmentTree:
    def __init__(self,n,nums):
        self.n=n
        self.nums=nums
        self.tree=[0]*(n*4)
        self.lazy=[0]*(n*4)
        self.build(1,1,n)
    def pushup(self,node):
        self.tree[node]=max(self.tree[node*2],self.tree[node*2+1])
    def pushdown(self,node,l,r):
        if(self.lazy[node]!=0):
            mid=(l+r)>>1
            self.tree[node*2]+=self.lazy[node]
            self.tree[node*2+1]+=self.lazy[node]
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
            self.tree[node]+=val
            self.lazy[node]+=val
            return
        if(end<l or start>r):
            return
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        self.update_range(node*2,start,mid,l,r,val)
        self.update_range(node*2+1,mid+1,end,l,r,val)
        self.pushup(node)
    def query(self,node,start,end,l,r):
        if(l<=start and end<=r):
            return self.tree[node]
        if(end<l or start>r):
            return 0
        self.pushdown(node,start,end)
        mid=(start+end)>>1
        return max(self.query(node*2,start,mid,l,r),self.query(node*2+1,mid+1,end,l,r))
n,q=map(int,input().split())
tree=SegmentTree(n,[0]*(n+1))
for _ in range(q):
    s=input().split()
    op=s[0]
    if(op=='Add'):
        l,r,v=map(int,s[1:])
        tree.update_range(1,1,n,l,r,v)
    elif(op=="Query"):
        l,r=map(int,s[1:])
        print(tree.query(1,1,n,l,r))
```



<mark>（至少包含有"Accepted"）</mark>


![](https://ik.imagekit.io/Amyxue/26spring-Assignment/Amy_Tu1qWorlF)



## 2. 学习总结和个人收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2026spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>


月考T5学习了找欧拉路径的方法，主要难点在于建图的思路，将字母看作节点。

额外练习题
 [【模板】缩点](https://www.luogu.com.cn/problem/P3387)
Tarjan缩点，将图变为DAG.然后进行拓扑排序，dp最大权值和，注意dp需要在拓扑序上进行以保证正确更新。
```python
from collections import deque
import sys
sys.setrecursionlimit(1000000)
n,m=map(int,input().split())
p=[0]+list(map(int,input().split()))
a=[[]for _ in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    a[x].append(y)
dfn=[0]*(n+1)
low=[0]*(n+1)
time=0
s=[]
scc=[]
idx=[0]*(n+1)
val=[]
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
        sum=0
        while(True):
            x=s.pop()
            tmp.append(x)
            sum+=p[x]
            idx[x]=len(scc)
            if(x==k):
                break
        scc.append(tmp)
        val.append(sum)
for i in range(1,n+1):
    if(dfn[i]==0):
        tarjan(i)
lens=len(scc)
in_deg=[0]*lens
dag=[[]for _ in range(lens)]
for i in range(1,n+1):
    for j in a[i]:
        if(idx[i]!=idx[j]):
            in_deg[idx[j]]+=1
            dag[idx[i]].append(idx[j])
q=deque()
dp=[0]*lens
for i in range(lens):
    if(in_deg[i]==0):
        q.append(i)
        dp[i]=val[i]
while(q):
    x=q.popleft()
    for i in dag[x]:
        dp[i]=max(dp[i],dp[x]+val[i])
        in_deg[i]-=1
        if(in_deg[i]==0):
            q.append(i)
print(max(dp))
```
[【模板】最小斯坦纳树](https://www.luogu.com.cn/problem/P6192)
上完课把模板打了一遍。学习了枚举子集的技巧。
先跑一遍Floyd计算任意两点间的最短路，然后状压dp枚举每个状态（s的子集）的子集，最短长度可以由两个子集的dp值更新。每个状态dp完之后使用dijkstra进行松弛操作，以得到对于状态mask的单源最短路。最后答案取以1-n为根的dp值中的最小值。
```cpp
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<queue>
using namespace std;
const int INF=0x3f3f3f3f;
int a[101][101];
int dp[1<<10][101];//j为根，将i中的关键点全部联通的最短距离
int n,m,k;
void dijkstra(int x){
    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> q;
    for(int i=1;i<=n;i++){
        if(dp[x][i]<INF){
            q.push({dp[x][i],i});
        }
    }
    while(!q.empty()){
        auto [dist,u]=q.top();
        q.pop();
        if(dist>dp[x][u]){
            continue;
        }
        for(int v=1;v<=n;v++){
            int w=a[u][v];
            if(dp[x][v]>dp[x][u]+w){
                dp[x][v]=dp[x][u]+w;
                q.push({dp[x][v],v});
            }
        }
    }
}
int main(){
    scanf("%d %d %d",&n,&m,&k);
    memset(a,INF,sizeof(a));
    for(int i=0;i<m;i++){
        int u,v,w;
        scanf("%d %d %d",&u,&v,&w);
        if(a[u][v]>w){
            a[u][v]=w;
            a[v][u]=w;
        }
    }
    int s[k];
    for(int i=0;i<k;i++){
        scanf("%d",&s[i]);
    }
    for(int p=1;p<=n;p++){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                a[i][j]=min(a[i][j],a[i][p]+a[p][j]);
            }
        }
    }
    memset(dp,INF,sizeof(dp));
    for(int i=1;i<(1<<k);i++){
        if(!(i&(i-1))){//i只有1个1
            for(int j=0;j<k;j++){
                if(i&(1<<j)){
                    dp[i][s[j]]=0;
                    break;
                }
            }
        }
        for(int j=i;j>0;j=(j-1)&i){//枚举i的子集
            for(int p=1;p<=n;p++){
                dp[i][p]=min(dp[i][p],dp[j][p]+dp[i^j][p]);
            }
        }
        dijkstra(i);
    }
    int ans=INF;
    for(int i=1;i<=n;i++){
        ans=min(ans,dp[(1<<k)-1][i]);
    }
    printf("%d\n",ans);
}
```
[简单题](https://www.luogu.com.cn/problem/P4148)
KD Tree模板题。补的之前讲树的时候没来得及写的板子。
```cpp
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
const int MAXN=200005;
const double alpha=0.75;//替罪羊树平衡因子
struct Node{
    int x,y;
    int v,sum;
    int x1,y1,x2,y2;
    int l,r;
    int size;
} t[MAXN];
int root,tot;
int cur_nodes[MAXN],node_cnt;
bool cmpx(int a,int b){
    return t[a].x<t[b].x;
}
bool cmpy(int a,int b){
    return t[a].y<t[b].y;
}
void push_up(int u){
    int l=t[u].l,r=t[u].r;
    t[u].size=t[l].size+t[r].size+1;
    t[u].sum=t[l].sum+t[r].sum+t[u].v;
    t[u].x1=min({t[u].x,t[l].x1,t[r].x1});
    t[u].y1=min({t[u].y,t[l].y1,t[r].y1});
    t[u].x2=max({t[u].x,t[l].x2,t[r].x2});
    t[u].y2=max({t[u].y,t[l].y2,t[r].y2});
}
void flatten(int u){//替罪羊树思想：不平衡时拍平子树重构
    if(!u) return;
    cur_nodes[node_cnt++]=u;
    flatten(t[u].l);
    flatten(t[u].r);
}
int build(int l,int r,int dim){
    if(l>r) return 0;
    int mid=(l+r)>>1;
    if(dim==0){
        nth_element(cur_nodes+l,cur_nodes+mid,cur_nodes+r+1,cmpx);
    }
    else{
        nth_element(cur_nodes+l,cur_nodes+mid,cur_nodes+r+1,cmpy);
    }
    int u=cur_nodes[mid];
    t[u].l=build(l,mid-1,dim^1);
    t[u].r=build(mid+1,r,dim^1);
    push_up(u);
    return u;
}
void insert(int &u,int p,int dim){
    if(!u){
        u=p;
        push_up(u);
        return;
    }
    if(dim==0){
        if(t[p].x<t[u].x){
            insert(t[u].l,p,dim^1);
        }
        else{
            insert(t[u].r,p,dim^1);
        }
    }
    else{
        if(t[p].y<t[u].y){
            insert(t[u].l,p,dim^1);
        }
        else{
            insert(t[u].r,p,dim^1);
        }
    }
    push_up(u);
    if(t[u].size*alpha<max(t[t[u].l].size,t[t[u].r].size)){
        node_cnt=0;
        flatten(u);
        u=build(0,node_cnt-1,dim);
    }
}
int query(int u,int x1,int y1,int x2,int y2){
    if(!u) return 0;
    if(t[u].x1>=x1 && t[u].y1>=y1 && t[u].x2<=x2 && t[u].y2<=y2){
        return t[u].sum;
    }
    if(t[u].x2<x1 || t[u].y2<y1 || t[u].x1>x2 || t[u].y1>y2){
        return 0;
    }
    int res=0;
    if(t[u].x>=x1 && t[u].x<=x2 && t[u].y>=y1 && t[u].y<=y2){
        res+=t[u].v;
    }
    res+=query(t[u].l,x1,y1,x2,y2);
    res+=query(t[u].r,x1,y1,x2,y2);
    return res;
}
int main(){
    t[0].x1=t[0].y1=2e9;
    t[0].x2=t[0].y2=-2e9;
    t[0].sum=t[0].size=0;
    int n;
    scanf("%d",&n);
    int op;
    int last_ans=0;
    while(scanf("%d",&op) && op!=3){
        if(op==1){
            int x,y,A;
            scanf("%d %d %d",&x,&y,&A);
            x^=last_ans;
            y^=last_ans;
            A^=last_ans;
            tot++;
            t[tot].x=x;
            t[tot].y=y;
            t[tot].v=t[tot].sum=A;
            insert(root,tot,0);
        }
        else if(op==2){
            int x1,y1,x2,y2;
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            x1^=last_ans;
            y1^=last_ans;
            x2^=last_ans;
            y2^=last_ans;
            last_ans=query(root,x1,y1,x2,y2);
            printf("%d\n",last_ans);
        }
    }
}
```


