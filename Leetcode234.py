from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(head):
        cur=head
        if(cur==None):
            return None
        qaq=cur.next
        head.next=None
        while(qaq!=None):
            tmp=qaq.next
            qaq.next=cur
            cur=qaq
            qaq=tmp
        return cur
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while(fast.next!=None and fast.next.next!=None):
            slow=slow.next
            fast=fast.next.next
        head2=Solution.reverseList(slow)
        head1=head
        if(head1.val!=head2.val):
            return False
        while(head1.next!=None and head2.next!=None):
            head1=head1.next
            head2=head2.next
            if(head1.val!=head2.val):
                return False
        return True
def init(arr):
    head=ListNode(arr[0])
    cur=head
    for i in range(1,len(arr)):
        cur.next=ListNode(arr[i])
        cur=cur.next
    return head
arr=[1,2,3,2,1]
print(Solution().isPalindrome(init(arr)))