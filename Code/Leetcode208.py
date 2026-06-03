class TreeNode:
    def __init__(self):
        self.children=[None]*26
        self.isEnd=False
class Trie:
    def __init__(self):
        self.root=TreeNode()
    def searchprefix(self,word):
        node=self.root
        for c in word:
            idx=ord(c)-ord('a')
            if(node.children[idx]==None):
                return None
            node=node.children[idx]
        return node
    
    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            idx=ord(c)-ord('a')
            if(node.children[idx]==None):
                node.children[idx]=TreeNode()
            node=node.children[idx]
        node.isEnd=True

    def search(self, word: str) -> bool:
        node=self.searchprefix(word)
        return node!=None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchprefix(prefix) != None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)