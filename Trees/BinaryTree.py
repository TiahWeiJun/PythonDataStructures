import sys

sys.path.insert(1, '/Users/Admin/Documents/Projects/DSA/Nodes')

sys.path.insert(1, '/Users/Admin/Documents/Projects/DSA/Stacks')


from Stacks import Stack
from Nodes import Node

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return '{}'.format(self.value)


class BinaryTree:
    def __init__(self, TreeNode):
        self.root = TreeNode

    #Pre-Order Traversal: Node -> Left -> Right
    def pre_order_traversal(self, start , traversal=[]):
        if start:
            traversal.append(start.value)
            traversal = self.pre_order_traversal(start.left, traversal)
            traversal = self.pre_order_traversal(start.right, traversal)
        return traversal

    #In-Order Traversal: Left -> Node -> Right 
    def in_order_traversal(self, start , traversal=[]):
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal.append(start.value)
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    #Post-Order Traversal: Left -> Right -> Node
    def post_order_traversal(self, start , traversal=[]):
        if start:
            traversal = self.post_order_traversal(start.left, traversal)
            traversal = self.post_order_traversal(start.right, traversal)
            traversal.append(start.value)
        return traversal

    #Level-Order Traversal
    def level_order_traversal(self):
        to_traverse = [self.root]
        traversal = []
        while len(to_traverse) > 0:
            node = to_traverse[0]
            data = node.value
            traversal.append(data)
            if node.left:
                to_traverse.append(node.left)
            if node.right:
                to_traverse.append(node.right)
            to_traverse.pop(0)
        return traversal

    #Reverse Level-Order Traversal
    def reverse_level_order(self):
        to_traverse = [self.root]
        stack = Stack(100)
        while len(to_traverse) > 0:
            node = to_traverse[0]
            data = node.value
            stack.push(Node(data))
            if node.right:
                to_traverse.append(node.right)
            if node.left:
                to_traverse.append(node.left)
            to_traverse.pop(0)
        traversal = []
        for x in range(stack.size):
            traversal.append(stack.pop().get_value())
        return traversal
        
    #Getting height of Tree
    def get_height(self, node):
        if not node:
            return -1
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        return 1 + max(left_height, right_height)

    #Getting size of tree
    def get_size(self):
        string = self.pre_order_traversal(self.root).replace(" ","")
        return len(string)


a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)
a7 = TreeNode(7)


tree = BinaryTree(a1)
tree.root.left = a2
tree.root.right = a3
tree.root.left.left = a4
tree.root.left.right = a5
tree.root.right.left = a6
tree.root.right.right = a7

print(tree.reverse_level_order())