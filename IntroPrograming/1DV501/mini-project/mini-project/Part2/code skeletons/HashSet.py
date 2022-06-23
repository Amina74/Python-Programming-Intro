
from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash_string = ''
        for char in word:
            if char.isdigit():
                int_char = int(char)
            else:
                int_char = abs(ord(char)-97)
            hash_string += str(int_char)
        hash = int(hash_string) % self.bucket_list_size()
        return hash

    # Doubles size of bucket list

    def rehash(self):
        new_bucket_size = 2*(self.bucket_list_size())
        temp = self.buckets
        new_buckets = [[] for i in range(new_bucket_size)]
        self.buckets = new_buckets
        for bucket in temp:
            for element in bucket:
                index = self.get_hash(element)
                new_buckets[index].append(element)

    # Adds a word to set if not already added

    def add(self, word):
        if not self.contains(word):
            index = self.get_hash(word) % self.bucket_list_size()
            self.buckets[index].append(word)

            if self.get_size() == self.bucket_list_size():
                self.rehash()

    # Returns a string representation of the set content

    def to_string(self):
        string = '{ '
        for bucket in self.buckets:
            for element in bucket:
                string = string + element + " "
        string += '}'
        return string

    # Returns current number of elements in set
    def get_size(self):
        size = 0
        for bucket in self.buckets:
            size += len(bucket)
        return size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        found = False
        hash = self.get_hash(word)
        for element in self.buckets[hash]:
            if element == word:
                found = True
        return found

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set

    def remove(self, word):
        index = self.get_hash(word)
        if word in self.buckets[index]:
            self.buckets[index].remove(word)

    # Returns the size of the bucket with most elements

    def max_bucket_size(self):
        largest_bucket = 0
        for bucket in self.buckets:
            if len(bucket) > largest_bucket:
                largest_bucket = len(bucket)
        return largest_bucket
