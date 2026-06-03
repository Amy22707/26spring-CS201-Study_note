from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None):
            return False
        a=set()
        cur=head
        a.add(cur)
        while(cur.next!=None):
            cur=cur.next
            if(cur in a):
                return True
            a.add(cur)
        return False