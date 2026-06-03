from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

a=[4,1,8,4,5]
b=[5,6,1,8,4,5] 
# 注意：这里直接生成的b包含后续节点，但为了模拟相交，我们会把b的尾部截断并接上a的相交部分
headA = create_linked_list(a)
headB = create_linked_list(b[:3]) # 只生成 [5,6,1]

# 模拟相交：相交点是 8
# a中8的位置是索引2 (4->1->8)
intersect_node = headA.next.next 

# 将b的尾部接上相交节点
curB = headB
while curB.next:
    curB = curB.next
curB.next = intersect_node

print(f"Intersect val: {Solution().getIntersectionNode(headA, headB).val}")