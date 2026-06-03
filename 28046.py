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