class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return "{}".format(self.value)
        
    def get_next_node(self):
        return self.next

    def set_next_node(self, Node):
        self.next = Node
    
    def get_value(self):
        return self.value


