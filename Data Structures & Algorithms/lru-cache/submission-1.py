class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        # key to Node
        self.cap = capacity

        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # put rightmost
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        prv.next = node
        node.prev = prv
        node.next = self.right
        self.right.prev = node
    
    # delete node
    def delete(self, node):
        nxt, prv = node.prev, node.next
        nxt.next = prv
        prv.prev = nxt
        node.next = node.prev = None
        

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.delete(node) # delete node
            self.insert(node) # insert rightmost 
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self.delete(self.map[key])
            self.insert(self.map[key]) # insert rightmost
        else:
            self.map[key] = Node(key, value)
            if len(self.map) > self.cap:
                del self.map[self.left.next.key]
                self.delete(self.left.next)
            self.insert(self.map[key])
                


# right = recent
# left = least recent
# get = if exists, put node to right and return value. Else, return -1
# put = if exists, update with new Node and put Node to right. If it
# does not exist, if capacity, delete leftmost node, if not, create new Node
# and put to rightmost
        
