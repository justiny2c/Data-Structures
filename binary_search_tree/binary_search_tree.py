from dll_stack import Stack
from dll_queue import Queue
import sys
sys.path.append('../queue_and_stack')

# If smaller go left
# if bigger or equal go right
# Does not have to be balanced?
# Negative numbers are not
# allowed?
# Not sure how it handles chars
# When deleting, smaller child
# becomes parent
# Deleting root, replace with largest node on left side
# Root starts as first node and stays unless deleted


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            # Go left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)  # needs to keep going left (RECURSION)
        else:
            # Go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            # Go left
            if not self.left:
                # It's not here
                return False
            else:
                return self.left.contains(target)
        else:  # Target is >= self.value
            # Go right
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # Keep going right to get max

        # if not self.right:
        #     return self.value
        # return self.right.get_max()

        max_value = self.value
        current = self

        while current:
            # if current is greather than max
            if current.value > max_value:
                max_value = current.value
            # then go right
            current = current.right
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if node:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        self.queue = Queue()
        if node:
            self.queue.enqueue(node)
            print(node.value)
            self.queue.dequeue()
            node.bft_print(node.left)
            node.bft_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        if node:
            print(node.value)
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
