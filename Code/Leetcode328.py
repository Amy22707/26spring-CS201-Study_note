from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        oddhead=head
        evenhead=head.next
        odd=oddhead
        even=evenhead
        while(even and even.next):
            t1=even.next
            even.next=t1.next
            odd.next=t1
            odd=odd.next
            even=even.next
        odd.next=evenhead
        return head
