import sys

sys.path.insert(1, '/Users/Admin/Documents/Python Data Structures/Nodes')

from Nodes import Node


class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    #Visual representation of linked list
    def visual(self):
        arr = []
        current_node = self.head
        while current_node and current_node.get_next_node() != self.head:
            arr.append(current_node)
            current_node = current_node.get_next_node()
        arr.append(current_node)
        print(arr)

    #Adding Node to end of list
    def append(self, Node):
        if not self.head:
            self.head = Node
            self.head.set_next_node(self.head)
        else:
            curr = self.head
            while curr.get_next_node() != self.head:
                curr = curr.get_next_node()
            curr.set_next_node(Node)
            Node.set_next_node(self.head)
            
            

    #Adding Node to start of list
    def prepend(self, Node):
        if not self.head:
            self.head = Node
            self.head.set_next_node(self.head)
        else:
            temp1 = self.head
            temp2 = self.head
            Node.set_next_node(self.head)
            self.head = Node
            while temp2.get_next_node() != temp1:
                temp2 = temp2.get_next_node()
            temp2.set_next_node(self.head)
            
    #Removing specicified Node
    def remove(self, Node):
        if self.head == Node and self.head.get_next_node() == self.head:
            self.head = None

        elif self.head == Node and self.head.get_next_node() != self.head:
            temp = self.head
            self.head = self.head.get_next_node()
            curr = self.head
            while curr.get_next_node() != temp:
               curr = curr.get_next_node()
            curr.set_next_node(self.head)
        else:
            curr = self.head
            prev = None
            while curr and curr != Node:
                prev = curr
                curr = curr.get_next_node()
            if curr.get_next_node() == self.head:
                prev.set_next_node(self.head)
            else:
                prev.set_next_node(curr.get_next_node())

    #Getting length of circular list
    def get_length(self):
        count = 0
        curr = self.head
        while curr and curr.get_next_node() != self.head:
            count += 1
            curr = curr.get_next_node()
        count += 1
        return count

    #Split linked list
    def split_list(self):
        length = self.get_length()
        if length == 0:
            return None
        if length == 1:
            return self.head
        
        num_iter = length//2

        curr = self.head
        prev = None
        for x in range(int(num_iter)):
            prev = curr
            curr = curr.get_next_node()
        prev.set_next_node(self.head)
        newList = CircularLinkedList()
        
        while curr.get_next_node() != self.head:
            next = curr.get_next_node()
            newList.append(curr)
            curr = next
        newList.append(curr)

        self.visual()
        newList.visual()

    #Josephus Problem
    def josephus_prob(self, step):
        if self.get_length() == 0:
            self.visual()
        elif self.get_length() == 1:
            self.visual()
        else:
            curr = self.head
            while curr and self.get_length() != 1:
                for x in range(int(step - 1)):
                    curr = curr.get_next_node()
                next = curr.get_next_node()
                self.remove(curr)
                curr = next
            self.visual()

#Checking is a list is a circular linked list
def is_circular_list(lst):
    curr = lst.head
    while curr:
        if curr.get_next_node() == lst.head:
            return True
        else:
            curr = curr.get_next_node()
    return False

        



            
                
    
a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)


cl = CircularLinkedList()
cl.append(a3)
cl.append(a4)
cl.append(a5)
cl.visual()












