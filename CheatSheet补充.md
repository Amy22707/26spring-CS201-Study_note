ICPC 2023 WF 一个递推问题
```cpp
#include <algorithm>
#include <cstring>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int64_t memo1[51];
int64_t count1(int64_t n) {
  if (n == 0) return 1;
  int64_t& ret = memo1[n];
  if (ret) return ret;
  for (int64_t a = 1; a <= n; a++)
  for (int64_t c = 1; a*c <= n; c++) {
    ret += count1(n - a*c);
  }
  return ret;
}

// Returns # of possible next elements for generated sequences matching "seq".
map<pair<vector<int64_t>, vector<int64_t>>, map<int64_t,int64_t>> memo;
vector<int64_t> curc, cura;
vector<tuple<vector<int64_t>, vector<int64_t>, vector<int64_t>>> saved;
const map<int64_t,int64_t>& count(vector<int64_t> seq, vector<int64_t> prev, bool save) {
  static map<int64_t,int64_t> empty{}, base{{0,1}};
  if (seq[0] == 0) {
    for (int i = 1; i < seq.size(); i++) if (seq[i]) return empty;
    if (save) {
      vector<int64_t> curs = cura;
      while (curs.size() < curc.size()+30) {
        int64_t x = 0;  // There may be some overflow, but this shouldn't affect relative sorting.
        for (int i = 0; i < curc.size(); i++) x += curs[curs.size()-curc.size()+i] * curc[i];
        curs.push_back(x);
      }
      curs.erase(curs.begin(), curs.begin()+curc.size());
      saved.push_back({curs, curc, cura});
    }
    return base;
  }
  for (auto x : seq) if (x <= 0) return empty;

  if (seq.size() >= 2) {
    vector<int64_t> seq2 = seq, prev2 = prev;
    seq2.pop_back(); prev2.pop_back();
    auto it = memo.find({seq2, prev2});
    if (it == memo.end() || !it->second.count(seq.back())) return empty;
  }

  auto [it, inserted] = memo.insert({{seq, prev}, empty});
  map<int64_t,int64_t>& ret = it->second;
  if (save) { ret.clear(); inserted = true; }
  if (!inserted) return ret;

  prev.insert(prev.begin(), 0);
  for (int64_t c = 1;   c <= seq[0]; c++)
  for (int64_t a = 1; a*c <= seq[0]; a++) {
    prev[0] = a;
    for (int i = 0; i < seq.size(); i++) seq[i] -= prev[i]*c;
    int64_t tmp = prev.back();
    prev.pop_back();

    if (save) { curc.insert(curc.begin(), c); cura.insert(cura.begin(), a); }
    for (auto [v, n] : count(seq, prev, save)) ret[v + tmp*c] += n;
    if (save) { curc.erase(curc.begin()); cura.erase(cura.begin()); }

    prev.push_back(tmp);
    for (int i = 0; i < seq.size(); i++) seq[i] += prev[i]*c;
  }
  return ret;
}

int main() {
  int64_t N;
  while (cin >> N) {
    memo.clear(); cura.clear(); curc.clear(); saved.clear();

    vector<int64_t> seq;
    for (int64_t n = 1; ; n++) {
      if (count1(n) < N) N -= count1(n); else { seq.push_back(n); break; }
    }
    while (seq.size() < 30 && seq.back() < 1e16) {
      auto m = count(seq, seq, false);
      int64_t tot = 0;
      for (auto [v, n] : m) {
        if (n < N) {
          N -= n;
        } else {
          seq.push_back(v);
          if (n <= 20) goto done;  // Small enough to brute force.
          break;
        }
      }
    }
done:

    count(seq, seq, true);
    sort(saved.begin(), saved.end());
    auto [sv, cv, av] = saved[N-1];
    cout << cv.size() << endl;
    for (int i = 0; i < cv.size(); i++) { if (i) cout << ' '; cout << cv[i]; }
    cout << endl;
    for (int i = 0; i < av.size(); i++) { if (i) cout << ' '; cout << av[i]; }
    cout << endl;
    for (int i = 0; i < 10; i++) { if (i) cout << ' '; cout << sv[i]; }
    cout << endl;
  }
}
```
Reference:https://github.com/raihanulislam00/47th-ICPC-World-Final-2023

往年期末题拾遗
0-W最小生成树:bfs求所有连通块并标记，然后对连通块跑MST.
```python
from collections import deque
n,m=map(int,input().split())
g=[[]for _ in range(n+1)]
edges=[]
for i in range(m):
    u,v,w=map(int,input().split())
    g[u].append(v)
    g[v].append(u)
    edges.append((w,u,v))
par=[0]*(n+1)
q=deque()
un_vis=[i for i in range(1,n+1)]
marked=[0]*(n+1)
cnt=0
while(un_vis):
    cnt+=1
    start=un_vis.pop()
    q.append(start)
    par[start]=cnt
    while(q):
        idx=q.popleft()
        for i in g[idx]:
            marked[i]=1
        nxt=[]
        for i in un_vis:
            if(marked[i]==0):
                q.append(i)
                par[i]=cnt
            else:
                nxt.append(i)
        un_vis=nxt
        for i in g[idx]:
            marked[i]=0
fa=[i for i in range(cnt+1)]
def find(x):
    if(x==fa[x]):
        return x
    fa[x]=find(fa[x])
    return fa[x]
def merge(x,y):
    fx=find(x)
    fy=find(y)
    if(fx==fy):
        return
    fa[fx]=fy
new_edges=[]
for w,u,v in edges:
    if(par[u]!=par[v]):
        new_edges.append((w,par[u],par[v]))
new_edges=sorted(new_edges,key=lambda x:x[0])
ans=0
tot=cnt-1
qwq=0
for w,u,v in new_edges:
    if(qwq==tot):
        break
    if(find(u)!=find(v)):
        merge(u,v)
        ans+=w
        qwq+=1
print(ans)
```
神经网络：拓扑序上dp
```python
from collections import deque
import sys
n,p=map(int,input().split())
a=[0]
b=[0]
for i in range(n):
    u,v=map(int,input().split())
    a.append(u)
    b.append(v)
g=[[]for _ in range(n+1)]
in_deg=[0]*(n+1)
out_deg=[0]*(n+1)
for i in range(p):
    u,v,w=map(int,input().split())
    g[u].append((v,w))
    in_deg[v]+=1
    out_deg[u]+=1
    if(v==u):
        print("NULL")
        sys.exit(0)
q=deque()
cnt=0
for i in range(1,n+1):
    if(in_deg[i]==0):
        q.append(i)
        cnt+=1
while(q):
    idx=q.popleft()
    if(a[idx]<=0):
        a[idx]=0
    for i,w in g[idx]:
        a[i]+=w*a[idx]
        in_deg[i]-=1
        if(in_deg[i]==0):
            cnt+=1
            a[i]-=b[i]
            q.append(i)
flag=0
if(cnt<n):
    print("NULL")
else:
    for i in range(1,n+1):
        if(out_deg[i]==0 and a[i]>0):
            flag=1
            print(i,a[i])
    if(flag==0):
        print("NULL")

```
没有上司的舞会：树形dp
```python
import sys
sys.setrecursionlimit(10**7)
n=int(input())
a=[0]
for i in range(n):
    r=int(input())
    a.append(r)
up=[[]for _ in range(n+1)]
down=[[]for _ in range(n+1)]
in_deg=[0]*(n+1)
for i in range(n-1):
    l,k=map(int,input().split())
    up[l].append(k)
    down[k].append(l)
    in_deg[l]+=1
dp1=[0]*(n+1)#i号节点参加，最大值
dp2=[0]*(n+1)#i号节点不参加，最大值
root=0
for i in range(1,n+1):
    if(in_deg[i]==0):
        root=i
        break
def dfs(x):
    dp1[x]=a[x]
    for i in down[x]:
        dfs(i)
        dp1[x]+=dp2[i]
        dp2[x]+=max(dp1[i],dp2[i])
dfs(root)
print(max(dp1[root],dp2[root]))
```
Okabe and Boxes
贪心：重排之后清空，如果要取出的时候栈为空则说明可以随便取。否则重排一次。
```python
n=int(input())
s=[]
cnt=0
res=1
for i in range(2*n):
    a=input()
    if(a[0]=='a'):
        op,num=a.split()
        s.append(int(num))
    else:
        if(s and s[-1]==res):
            s.pop()
            res+=1
        elif(len(s)==0):
            res+=1
            continue
        else:
            cnt+=1
            s.clear()
            res+=1
print(cnt)

```