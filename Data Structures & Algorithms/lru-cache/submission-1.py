class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.vals = {}
        self.linkedList = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        self.refresh(key)
        return self.vals[key].val
        
    def put(self, key: int, value: int) -> None:
        if key in self.vals:
            self.vals[key].val = value
            self.refresh(key)
        else:
            self.vals[key] = Node(key, value)
            self.refresh(key)
            if len(self.vals) > self.cap:
                deleted = self.linkedList.removeHead()
                del self.vals[deleted.key]


    def refresh(self, key):
        node = self.vals[key]
        refreshNode = self.linkedList.removeNode(node)
        self.linkedList.add(refreshNode)

class Node:
    def __init__(self, key = 0, val = 0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def add(self, node):
        node.prev = node.next = None

        if self.head == None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        if prevNode: prevNode.next = nextNode
        if nextNode: nextNode.prev = prevNode

        if self.head == node:
            self.head = nextNode
        
        if self.tail == node:
            self.tail = prevNode

        node.prev = node.next = None
        return node

    def removeHead(self):
        return self.removeNode(self.head)
        