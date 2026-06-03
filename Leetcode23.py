# Definition for singly-linked list.
from typing import List, Optional
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self,other):
        return self.val<other.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        n=len(lists)
        for i in range(n):
            if(lists[i]):
                heapq.heappush(h,(lists[i].val,i,lists[i]))
        dummy=cur=ListNode()
        while(h):
            val,index,node=heapq.heappop(h)
            cur.next=node
            cur=cur.next
            if(node.next):
                heapq.heappush(h,(node.next.val,index,node.next))
        return dummy.next