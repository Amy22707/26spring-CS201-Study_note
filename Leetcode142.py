from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        if(fast==None):
            return None
        if(fast.next==None):
            return None
        while(True):
            slow=slow.next
            fast=fast.next.next
            if(fast==None or fast.next==None):
                return None
            if(fast==slow):
                break
        cur=head
        while(slow!=cur):
            slow=slow.next
            cur=cur.next
        return cur