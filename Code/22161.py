import heapq
class Node:
    def __init__(self,weight,chars,left=None,right=None):
        self.weight=weight
        self.chars=sorted(list(chars))
        self.min_char=self.chars[0]
        self.left=left
        self.right=right
    def __lt__(self,other):
        if(self.weight!=other.weight):
            return self.weight<other.weight
        return self.min_char<other.min_char
def build(nodes):
    heapq.heapify(nodes)
    while(len(nodes)>1):
        left=heapq.heappop(nodes)
        right=heapq.heappop(nodes)
        new_weight=left.weight+right.weight
        new_chars=left.chars+right.chars
        parent=Node(new_weight,new_chars,left,right)
        heapq.heappush(nodes,parent)
    return nodes[0]
def decode(node,res,codes):
    if(not node.left and not node.right):
        codes[node.chars[0]]=res
        return
    if(node.left):
        decode(node.left,res+'0',codes)
    if(node.right):
        decode(node.right,res+'1',codes)

n=int(input())
nodes=[]
for i in range(n):
    char,freq=input().split()
    freq=int(freq)
    nodes.append(Node(freq,[char]))
root=build(nodes)
char_to_code={}
decode(root,'',char_to_code)
code_to_char={}
while(True):
    try:
        q=input()
        if(q[0] in "01"):
            res=""
            cur=root
            for c in q:
                if(c=='0'):
                    cur=cur.left
                else:
                    cur=cur.right
                if(not cur.left and not cur.right):
                    res+=cur.chars[0]
                    cur=root
        else:
            res=""
            for c in q:
                res+=char_to_code[c]
        print(res)
    except EOFError:
        break