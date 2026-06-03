from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        n=1
        while(cur.next!=None):
            n+=1
            cur=cur.next
        n=n//2
        cur=head
        while(n):
            cur=cur.next
            n-=1
        return cur