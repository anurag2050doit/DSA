"""
LRU Cache Implementation
How to implement LRU caching scheme? What data structures should be used?
We are given total possible page numbers that can be referred. We are also given cache (or memory) size (Number of page
frames that cache can hold at a time). The LRU caching scheme is to remove the least recently used frame when the cache
is full and a new page is referenced which is not there in cache. Please see the Galvin book for more details (see the
LRU page replacement slide here).

We use two data structures to implement an LRU Cache.

Queue which is implemented using a doubly linked list. The maximum size of the queue will be equal to the total number
of frames available (cache size). The most recently used pages will be near front end and least recently pages will be
near the rear end.
A Hash with page number as key and address of the corresponding queue node as value.
When a page is referenced, the required page may be in the memory. If it is in the memory, we need to detach the node of
 the list and bring it to the front of the queue.
If the required page is not in memory, we bring that in memory. In simple words, we add a new node to the front of the
queue and update the corresponding node address in the hash. If the queue is full, i.e. all the frames are full, we
remove a node from the rear of the queue, and add the new node to the front of the queue.


Example – Consider the following reference string :

1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Find the number of page faults using least recently used (LRU) page replacement algorithm with 3 page frames.
"""

from collections import OrderedDict


class DoubleLinkList:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        self.head = DoubleLinkList(-1, -1)
        self.tail = self.head
        self.length = 0

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        node = self.hash_map[key]
        value = node.value
        if node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            if node.next:
                node.next.prev = node.prev
                node.prev.next = node.next
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
            return
        node = DoubleLinkList(key, value)
        self.hash_map[key] = node
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.length += 1
        if self.length > self.capacity:
            remove = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
            del self.hash_map[remove.key]
            self.length -= 1
        return


# Your LRUCache object will be instantiated and called as such:


class LRUCacheOrderDic:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict_ = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dict_:
            return -1
        else:
            self.dict_.move_to_end(key)
            return self.dict_[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict_:
            self.dict_.move_to_end(key)
            self.dict_[key] = value
        else:
            if self.capacity > 0:
                self.dict_[key] = value
                self.capacity -= 1
            else:
                self.dict_.popitem(last=False)
                self.dict_[key] = value


if __name__ == '__main__':
    capacity = 2

    cache = LRUCache(capacity)
    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1))  # returns 1
    print(cache.put(3, 3))  # evicts key 2
    print(cache.get(2))  # returns -1 (not found)
    print(cache.put(4, 4))  # evicts key 1
    print(cache.get(1))  # returns -1 (not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4

    capacity = 2

    cache = LRUCacheOrderDic(capacity)
    print(cache.put(1, 1))
    print(cache.put(2, 2))
    print(cache.get(1))  # returns 1
    print(cache.put(3, 3))  # evicts key 2
    print(cache.get(2))  # returns -1 (not found)
    print(cache.put(4, 4))  # evicts key 1
    print(cache.get(1))  # returns -1 (not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4

    # print(cache.put(2, 1))
    # print(cache.put(1, 1))
    # print(cache.put(2, 3))
    # print(cache.put(4, 1))
    # print(cache.get(1))
    # print(cache.get(2))
