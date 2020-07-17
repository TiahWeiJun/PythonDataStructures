class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return "{}".format(self.value)


class DLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        arr = []
        if self.head:
            curr = self.head
            while curr:
                arr.append(curr)
                curr = curr.next
        return "{}".format(arr)

    #Get length
    def get_length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    #Adding to end of list
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            newNode.prev = curr

    #Adding to start of list
    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    #Reverse double linked list
    def reverse(self):
        curr = self.head
        nxt = curr.next
        prev = None
        while nxt:
            curr.next = prev
            curr.prev = nxt
            prev = curr
            curr = nxt
            nxt = nxt.next
        self.head = curr
        self.head.next = prev

    #Remove specific value/node
    def remove_value(self, value):
        if self.get_length() == 1:
            self.head = self.head.next
        elif self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
        else:
            curr = self.head
            prev = None
            while curr and curr.value != value:
                prev = curr
                curr = curr.next
            if curr.next:
                nxt = curr.next
                prev.next = curr.next
                nxt.prev = prev
            else:
                prev.next = None

    #Removing duplicates
    def remove_dups(self):
        ptr1 = self.head
        while ptr1:
            prev = ptr1
            ptr2 = ptr1.next
            while ptr2:
                if ptr1.value == ptr2.value:
                    if ptr2.next:
                        nxt = ptr2.next
                        prev.next = nxt
                        nxt.prev = prev
                        ptr2 = nxt
                    else:
                        prev.next = None
                        ptr2 = ptr2.next
                else:
                    prev = ptr2
                    ptr2 = ptr2.next
            ptr1 = ptr1.next

    #Adding node to sorted DLL(ascending order)
    def add_node_to_sorted(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            prev = None
            while curr:
                if value <= curr.value:
                    if not prev:
                        newNode.next = self.head
                        self.head.prev = newNode
                        self.head = newNode
                    else:
                        prev.next = newNode
                        newNode.prev = prev
                        newNode.next = curr
                        curr.prev = newNode
                    break
                else:
                    prev = curr
                    curr = curr.next
            prev.next = newNode
            newNode.prev = prev

                        

            

lst = DLL()
lst.append(2)
lst.append(4)
lst.append(6)
lst.append(8)
lst.append(10)
lst.append(12)

print(lst)
lst.add_node_to_sorted(13)
print(lst)