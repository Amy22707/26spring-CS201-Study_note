from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self,head,tail):
        cur1=head
        cur2=cur1.next
        while(cur1!=tail):
            cur3=cur2.next
            cur2.next=cur1
            cur1=cur2
            cur2=cur3
        return tail,head
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        while(head):
            head=pre.next
            tail=pre
            for i in range(k):
                tail=tail.next
                if(tail==None):
                    return dummy.next
            tmp=tail.next
            head,tail=Solution().reverse(head,tail)
            pre.next=head
            tail.next=tmp
            pre=tail
        return dummy.next
    def make(self,arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        cur = head
        for val in arr[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head
arr=[1,2,3,4,5]
head=Solution().make(arr)
k=3
head=Solution().reverseKGroup(head,k)
while(head):
    print(head.val)
    head=head.next