from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as first entry in deque
    def add_first(self, n):
        tmp = Node(n)
        if self.head is None:
            self.head = tmp
            self.size = 1
            self.tail = self.head
        else:
            tmp.nxt = self.head
            self.head = tmp
            self.size = self.size+1

    # Returns a string representation of the current deque content
    def to_string(self):
        s = "{"
        node = self.head
        while node is not None:
            s += str(node.value) + " " 
            node = node.nxt
        s += "}"    
        return s

    # Add element n as last entry in deque
    def add_last(self, n):
        tmp = Node(n)
        if self.size == 0:
            self.head = tmp
            self.size = 1
            self.tail = self.head
        else:
            self.tail.nxt=tmp
            self.tail = self.tail.nxt
            self.size += 1


    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if(self.size == 0):
            print("Queue is empty")
            return None
        else:
            return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if(self.size == 0):
            print("Queue is empty")
            return None
        else:
            return self.head.value


    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if(self.size == 0):
            print("Queue is empty")
            return
        curr = self.head

        if(self.size == 1):
            self.head = None
            self.tail = None
            self.size = 0
        else:
            self.head = self.head.nxt
            self.size -= 1

        del curr

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if(self.size == 0):
            print("Queue is empty")
            return

        if(self.size == 1):
            curr = self.head
            del curr
            self.head = None
            self.tail = None
            self.size = 0
        else:
            prev=self.head
            last = self.tail
            while prev.nxt!=last:
                prev=prev.nxt
            prev.nxt = None
            self.tail = prev
            self.size -= 1
            del last
