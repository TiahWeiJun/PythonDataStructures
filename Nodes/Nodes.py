class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return "{}".format(self.value)


a = Node(2)
b = Node(3)
a.next = b
