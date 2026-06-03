from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return None
        if(head.next==None):
            return head
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        while(cur.next!=None and cur.next.next!=None):
            cur1=cur.next
            cur2=cur.next.next
            cur1.next=cur2.next
            cur2.next=cur1
            cur.next=cur2
            cur=cur1
        return dummy.next
