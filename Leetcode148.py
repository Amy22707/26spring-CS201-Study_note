# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middle(self,head):
        slow=fast=head
        while(fast and fast.next):
            pre=slow
            slow=slow.next
            fast=fast.next.next
        pre.next=None
        return slow
    def merge(self,l1,l2):
        cur=dummy=ListNode()
        while(l1 and l2):
            if(l1.val<l2.val):
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        if(l1):
            cur.next=l1
        if(l2):
            cur.next=l2
        return dummy.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return head
        head2=self.middle(head)
        head=self.sortList(head)
        head2=self.sortList(head2)
        return self.merge(head,head2)