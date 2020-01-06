import time
import sys
sys.path.append('../ring_buffer')
from doubly_linked_list import DoublyLinkedList

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left:
                    return self.left.insert(value)
                else:
                    self.left = BinarySearchTree(value)
                    return self.left.value
            elif value >= self.value:
                if self.right:
                    return self.right.insert(value)
                else:
                    self.right = BinarySearchTree(value)
                    return self.right.value
        else:
            self.value = value
            return self.value

    def contains(self, target):
        if target == self.value:
            return True
        elif target >= self.value:
            if self.right:
                if self.right.value == target:
                    return True
                else:
                    return self.right.contains(target)
            else:
                return False
        elif target < self.value:
            if self.left:
                if self.left.value == target:
                    return True
                else:
                    return self.left.contains(target)
            else:
                return False
binTree = BinarySearchTree('1')
duplicates = []
for name in names_1:
    binTree.insert(name)
for name in names_2:
    if binTree.contains(name):
        duplicates.append(name)

# 
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?3