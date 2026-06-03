from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head
        if(head==None):
            return None
        while(cur):
            t=Node(cur.val)
            t.next=cur.next
            cur.next=t
            cur=t.next
        cur=head
        while(cur):
            if(cur.random):
                cur.next.random=cur.random.next
            cur=cur.next.next
        newhead=head.next
        cur=head
        newcur=Node(0,head)
        while(cur):
            copy=cur.next
            newcur.next=copy
            cur.next=copy.next
            cur=cur.next
            newcur=newcur.next
        return newhead