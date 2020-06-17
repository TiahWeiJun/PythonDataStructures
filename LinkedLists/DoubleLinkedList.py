class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return "{}".format(self.value)

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next
    
    def set_next_node(self, Node):
        self.next = Node
    
    def get_prev_node(self):
        return self.prev
    
    def set_prev_node(self, Node):
        self.prev = Node


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    #Visual representation of linked list
    def visual(self):
        arr = []
        current_node = self.head
        while current_node:
            arr.append(current_node)
            current_node = current_node.get_next_node()
        print(arr)
    
    #Adding to end of list
    def append(self, Node):
        if not self.head:
            self.head = Node
        else:
            curr = self.head
            while curr.get_next_node():
                curr = curr.get_next_node()
            curr.set_next_node(Node)
            Node.set_prev_node(curr)
            
            
    #Adding to start of list
    def prepend(self, Node):
        if not self.head:
            self.head = Node
        else:
            Node.set_next_node(self.head)
            self.head.set_prev_node(Node)
            self.head = Node

    #Reversing double linked list
    def reverse(self):
        temp = None
        curr = self.head
        while curr:
            temp = curr.get_prev_node()
            curr.set_prev_node(curr.get_next_node())
            curr.set_next_node(temp)
            curr = curr.get_prev_node()
        if temp:
            self.head = temp.get_prev_node()

    #Adding Node after specified node:
    def add_after(self, specified_node, Node):
        curr = self.head
        while curr and curr != specified_node:
            curr = curr.get_next_node()
        if curr.get_next_node():
            next = curr.get_next_node()
            curr.set_next_node(Node)
            Node.set_prev_node(curr)
            Node.set_next_node(next)
            next.set_prev_node(Node)
        else:
            curr.set_next_node(Node)
            Node.set_prev_node(curr)

    #Adding Node before specified node:
    def add_before(self, specified_node, Node):
        curr = self.head
        while curr and curr != specified_node:
            curr = curr.get_next_node()
        if curr.get_prev_node():
            prev = curr.get_prev_node()
            curr.set_prev_node(Node)
            Node.set_next_node(curr)
            Node.set_prev_node(prev)
            prev.set_next_node(Node)
        else:
            Node.set_next_node(curr)
            curr.set_prev_node(Node)
            self.head = Node

    #Removing specific Node
    def remove(self, Node):
        curr = self.head
        if curr == Node:
            self.head = curr.get_next_node()
            self.head.set_prev_node(None)
        else:
            while curr and curr != Node:
                curr = curr.get_next_node()
            prev = curr.get_prev_node()
            if not curr.get_next_node():
                prev.set_next_node(None)
            else:
                next = curr.get_next_node()
                prev.set_next_node(next)
                next.set_prev_node(prev)
    
    #Removing duplicates
    def remove_duplicates(self):
        curr = self.head
        while curr:
            pointer = curr.get_next_node()
            while pointer:
                if pointer.get_value() != curr.get_value():
                    pointer = pointer.get_next_node()
                else:
                    if not pointer.get_next_node():
                        prev = pointer.get_prev_node()
                        prev.set_next_node(None)
                    else:
                        next = pointer.get_next_node()
                        prev = pointer.get_prev_node()
                        prev.set_next_node(next)
                        next.set_prev_node(prev)

                    pointer = pointer.get_next_node()
   
            curr = curr.get_next_node()

    #Finding pairs with sum
    def pairs_with_sum(self, sum):
        pairlist = []
        curr = self.head
        while curr:
            next = curr.get_next_node()
            while next:
                if next.get_value() + curr.get_value() == sum:
                    pairlist.append([curr, next])
                next = next.get_next_node()
            curr = curr.get_next_node()
        return pairlist

a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)
a5 = Node(5)
a6 = Node(6)
a7 = Node(7)
a8 = Node(8)
a9 = Node(9)

dl = DoubleLinkedList()
dl.append(a1)
dl.append(a2)
dl.append(a3)
dl.append(a4)
dl.append(a5)
dl.append(a6)
dl.append(a7)
dl.append(a8)
dl.append(a9)
dl.visual()
list1 = dl.pairs_with_sum(10)
print(list1)


