class Node:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache=dict()
        self.capacity=capacity
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if(key not in self.cache):
            return -1
        node=self.cache[key]
        self.remove_node(node)
        self.add_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            node=self.cache[key]
            node.val=value
            self.remove_node(node)
            self.add_to_end(node)
        else:
            node=Node(key,value)
            self.cache[key]=node
            self.add_to_end(node)
        if(len(self.cache)>self.capacity):
            self.cache.pop(self.head.next.key)
            self.remove_node(self.head.next)

    def remove_node(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def add_to_end(self,node):
        node.prev=self.tail.prev
        node.prev.next=node
        node.next=self.tail
        self.tail.prev=node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
obj=LRUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))