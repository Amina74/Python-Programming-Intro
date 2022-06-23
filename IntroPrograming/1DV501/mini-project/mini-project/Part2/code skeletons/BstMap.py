from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        # add a new key, value pair to the Binary Search tree
        if key == self.key:
            self. value = value
        elif key < self.key:
            if self.left == None:
                self.left = Node(key, value, None, None)
            else:
                self.left.put(key, value)
        else:
            if self.right == None:
                self.right = Node(key, value, None, None)
            else:
                self.right.put(key, value)

    def to_string(self):
        # Returns a string representation of all the key-value pairs
        lst = []
        tuples = self.as_list(lst)
        map_string = ''
        for tuple in tuples:

            map_string += '(' + str(tuple[0]) + ',' + str(tuple[1]) + ') '

        return map_string

    def count(self):
        # Returns the number of key-value pairs in the binary search tree
        lst = []
        tuples = self.as_list(lst)
        return len(tuples)

    def get(self, key):
        # Returns the value for a given key. Returns None
        # if key doesn't exist
        queue = []
        queue.append(self)
        while queue:
            current_node = queue[0]
            queue.pop(0)
            if current_node.key == key:
                return current_node.value
            if current_node.left != None:
                queue.append(current_node.left)
            if current_node.right != None:
                queue.append(current_node.right)
        return None

    def max_depth(self):
        # Returns the maximum tree depth. That is, the length
        # (counted in nodes) of the longest root-to-leaf path
        left_depth = 0
        right_depth = 0
        if self.left != None:
            left_depth = self.left.max_depth()
        elif self.right != None:
            right_depth = self.right.max_depth()
        return max(left_depth, right_depth) + 1

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys

    def as_list(self, lst):
        # Returns a sorted list of all key-value pairs in the map.
        # Each key-value pair is represented as a tuple and the
        # list is sorted on the keys ==> left-to-right in-order
        if self.left != None:
            self.left.as_list(lst)
        lst.append((self.key, self.value))
        if self.right != None:
            self.right.as_list(lst)

        return lst


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
