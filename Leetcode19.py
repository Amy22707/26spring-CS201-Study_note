from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        fast=head
        for i in range(n-1):
            fast=fast.next
        # if(fast==None):
        #     return None
        if(fast.next==None):
            tmp=slow.next
            slow.next=None
            return tmp
        while(fast.next.next!=None):
            slow=slow.next
            fast=fast.next
        qaq=slow.next.next
        slow.next=qaq
        return head
        