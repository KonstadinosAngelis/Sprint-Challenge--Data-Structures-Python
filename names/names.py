import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# for each in names_1:
#     if each not in names_2:
#         duplicates.append(each)
# print(duplicates)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value <= value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        elif self.value > value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        if self.right is None and self.left is None:
            return

        if self.value == target:
            print("got here!")
            return target

        if self.value < target:
            if self.right.value is target:
                return target
            else:
                self.right.contains(target)

        if self.value > target:
            if self.left.value is target:
                return target
            else:
                self.left.contains(target)

test = BSTNode("connor")
test.insert("testing time!")
test.insert("testing time2!")
test.insert("testing time3!")
test.insert("testing time4!")
test.insert("testing time0!")

print(test.contains("testing time!2"))

# for n in names_1:
#     test.insert(n)

# for names in names_1:
#     print(test.contains(names))





end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
