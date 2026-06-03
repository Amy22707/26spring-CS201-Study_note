from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if(not root):
            return "[]"
        res=[]
        q=deque()
        q.append(root)
        while(q):
            node=q.popleft()
            if(node):
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append('null')
        return '['+','.join(res)+']'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(data=="['null']" or data=="[]"):
            return None
        val=data[1:-1].split(',')
        root=TreeNode(int(val[0]))
        q=deque()
        q.append(root)
        i=1
        while(q):
            node=q.popleft()
            if(val[i]!="null"):
                node.left=TreeNode(int(val[i]))
                q.append(node.left)
            i+=1
            if(val[i]!="null"):
                node.right=TreeNode(int(val[i]))
                q.append(node.right)
            i+=1
        return root  

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))