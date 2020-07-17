import sys

sys.path.insert(1, '/Users/tiahw/Documents/Projects/PythonDataStructures/Nodes')


from Nodes import Node

class CLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        arr = []
        if self.head:
            curr = self.head
            while curr.next != self.head:
                arr.append(curr)
                curr = curr.next
            arr.append(curr)
                
        return "{}".format(arr)

    #Length of CLL
    def get_length(self):
        count = 0
        if not self.head:
            return count
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
                count += 1
            count += 1
            return count


    #Adding node to end of list
    def append(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.head.next = newNode
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = newNode
            newNode.next = self.head
    
    #Adding node to start of list
    def prepend(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.head.next = newNode
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = newNode
            newNode.next = self.head
            self.head = newNode

    #Removing node with specific value
    def remove(self, value):
        if self.head.value == value:
            if not self.head.next:
                self.head = None
            else:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                curr.next = self.head.next
                self.head = self.head.next
        else:
            curr = self.head
            prev = None
            while curr and curr.value != value:
                prev = curr
                curr = curr.next
            if curr.next == self.head:
                prev.next = self.head
            else:
                prev.next = curr.next

    #Split linked list into two
    def split_list(self):
        if not self.head or not self.head.next:
            return
        num_iter = self.get_length()//2 - 1
        curr = self.head
        for x in range(num_iter):
            curr = curr.next
            nxt = curr.next
        lst1 = CLL()
        lst1.head = nxt
        ptr1 = lst1.head
        while ptr1.next != self.head:
            ptr1 = ptr1.next
        ptr1.next = lst1.head

        curr.next = self.head

        print(lst1)
        print(self)

    #Josephus problem
    def josephus_problem(self, step):
        if self.get_length() == 1 or self.get_length() == 0:
            return None
        curr = self.head
        prev = None
        while self.get_length() > 1:
            for x in range(step - 1):
                curr = curr.next
            nxt = curr.next
            self.remove(curr.value)
            curr = nxt

        return curr
            


        
            

        


                

lst = CLL()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)

print(lst)
print(lst.josephus_problem(3))












