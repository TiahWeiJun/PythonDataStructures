
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return '{}'.format(self.value)

class BST:
    def __init__(self):
        self.root = None

    #Getting size of tree
    def get_size(self):
        string = self.level_order_traversal().replace(" ","")
        return len(string)

    #In-Order Traversal
    def in_order_traversal(self, start , traversal=[]):
        if start:
            traversal = self.in_order_traversal(start.left, traversal)
            traversal.append(start.value)
            traversal = self.in_order_traversal(start.right, traversal)
        return traversal

    #Level Order Traversal
    def level_order_traversal(self):
        traversal = []
        if self.root:
            to_traverse = [self.root]
            while len(to_traverse) > 0:
                node = to_traverse[0]
                traversal.append(node.value)
                if node.left:
                    to_traverse.append(node.left)
                if node.right:
                    to_traverse.append(node.right)
                to_traverse.pop(0)
        return traversal
        

    #Inserting TreeNode to BST
    def insert(self, TreeNode):
        if not self.root:
            self.root = TreeNode
        else:
            self._insert(self.root,TreeNode)

    #Helper method for insert
    def _insert(self, start, TreeNode):
        if TreeNode.value < start.value:
            if start.left:
                self._insert(start.left, TreeNode)
            else:
                start.left = TreeNode
        elif TreeNode.value > start.value:
            if start.right:
                self._insert(start.right, TreeNode)     
            else:
                start.right = TreeNode   
        else:
            print("Data already exists in BST")

    #Searching BST for value:
    def is_in_BST(self, value):
        if not self.root:
            print(False)
        else:
            self._is_in_BST(self.root, value)
            
    #Helper Method for search
    def _is_in_BST(self, start, value):
        if value < start.value:
            if start.left:
                self._is_in_BST(start.left, value)
            else:
                print(False)
        elif value > start.value:
            if start.right:
                self._is_in_BST(start.right, value)
            else:
                print(False)
        else:
            print(True)

#Checking whether a tree is a BST
def is_BST(tree):
    if not tree.root:
        return False
    else:
        lst = tree.in_order_traversal(tree.root)
        for x in range(len(lst)-1):
            if lst[x] >= lst[x + 1]:
                return False
        return True
            


    





a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a6 = TreeNode(6)
a7 = TreeNode(7)



