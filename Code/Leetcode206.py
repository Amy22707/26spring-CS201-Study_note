from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
def init(arr):
    head=ListNode(arr[0])
    cur=head
    for i in range(1,len(arr)):
        cur.next=ListNode(arr[i])
        cur=cur.next
    return head
arr=[1,2,3,4,5]
print(Solution().reverseList(init(arr)).val)