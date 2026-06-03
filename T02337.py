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