# Use hashmap + double linked list

class Node:
    def __init__(self, key: int = None, value: int = None, next: "Node" = None, prev: "Node" = None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {} # map the keys to node
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.map.get(key)

        if not node:
            node = Node(key, value)
            self.map[key] = node

            self._push_node(node)
            if len(self.map) > self.capacity:
                tail = self._pop_tail()
                del self.map[tail.key]
        else:
            node.value = value
            self._move_to_head(node)

    def _push_node(self, node):
        # fix the head node, always add right after head
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _pop_tail(self):
        # fix the tail node, always pop the node before tail
        node = self.tail.prev
        self._remove_node(node)
        return node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._push_node(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)