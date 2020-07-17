import sys
import copy

sys.path.insert(1, '/Users/tiahw/Documents/Projects/PythonDataStructures/Nodes')

from Nodes import Node

class Queue:
    def __init__(self, limit):
        self.head = None
        self.tail = None
        self.size = 0
        self.limit = limit

    #Visual representation of queue
    def visual(self):
        lst = []
        duplicate = copy.copy(self)
        for x in range(duplicate.size):
            lst.append(duplicate.dequeue().get_value())
        print(lst)

    #Adding to back of queue
    def enqueue(self, Node):
        if self.limit > self.size:
            if self.size == 0:
                self.head = Node
                self.tail = Node
            else:
                self.tail.set_next_node(Node)
                self.tail = Node
            self.size += 1
        else:
            print("Queue reached its limit!")
            
    #Removing from front of queue
    def dequeue(self):
        node_to_remove = self.head
        if self.size != 0:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return node_to_remove
        else: 
            print("Queue is empty!")

    #Getting head node from front of queue
    def peek(self):
        if self.size != 0:
            return self.head
        else:
            print("Queue is empty!")

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)

q = Queue(100)
q.enqueue(a1)
q.enqueue(a2)

q.visual()
print(q.peek().get_value())
