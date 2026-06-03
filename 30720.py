from collections import deque
n,m=map(int,input().split())
a=list(map(int,input().split()))
class Node:
    def __init__(self,val=0):
        self.val=val
        self.win=val
        self.left=None
        self.right=None
        self.parent=None
leaves=[Node(x) for x in a]
q=deque(leaves)
while(len(q)>1):
    a=q.popleft()
    b=q.popleft()
    cur=Node()
    cur.val=max(a.win,b.win)
    cur.win=min(a.win,b.win)
    cur.left=a
    cur.right=b
    a.parent=b.parent=cur
    q.append(cur)
cur=q.popleft()
root=Node(cur.win)
root.left=cur
cur.parent=root
def bfs():
    res=[]
    qaq=deque()
    qaq.append(root)
    while(qaq and len(res)<n):
        cur=qaq.popleft()
        res.append(cur.val)
        if(cur.left):
            qaq.append(cur.left)
        if(cur.right):
            qaq.append(cur.right)
    return res
res=bfs()
print(*res)
for i in range(m):
    idx,val=map(int,input().split())
    cur=leaves[idx]
    cur.val=cur.win=val
    p=cur.parent
    while(p):
        if(p.right):
            p.val=max(p.left.win,p.right.win)
            p.win=min(p.left.win,p.right.win)
        else:
            p.val=p.win=p.left.win
        p=p.parent
    res=bfs()
    print(*res)