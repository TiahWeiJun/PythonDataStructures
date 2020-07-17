import sys

sys.path.insert(1, '/Users/Admin/Documents/Projects/DSA/Nodes')

from Nodes import Node

class SLL:
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

    #Length of SLL
    def get_length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    #Adding to start of SLL. O(1)
    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    #Adding to end of SLL. O(n)
    def append(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode

    #Removing Node by value. O(n)
    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
        else:
            curr = self.head
            nxt = curr.next
            while nxt:
                if nxt.value == value:
                    curr.next = nxt.next
                    return
                else:
                    curr = curr.next
                    nxt = curr.next
            print("Node not in linked list")
            
    #Removing specific Node by index(assuming list is zero indexed). O(n)
    def remove_by_index(self, index):
        if not isinstance(index, int):
            print("Please input integer value")

        if index >= self.get_length():
            print("Index is out of range")
        else:
            if index == 0:
                self.head = self.head.next
            else:
                curr = self.head
                prev = None
                for x in range(index):
                    prev = curr
                    curr = curr.next
                prev.next = curr.next

    #Remove from nth to last node. O(n)
    def remove_nth_last_node(self, n):
        if not isinstance(n, int):
            print("Please input integer value")
        if n >= self.get_length():
            print("Index is out of range")
        else:
            if n == self.get_length() - 1:
                self.head = self.head.next
            else:
                curr = self.head
                prev = None
                for x in range(self.get_length() - 1 - n):
                    prev = curr
                    curr = curr.next
                prev.next = curr.next

    #Reverse Linked List
    def reverse(self):
        prev = None
        curr = self.head
        nxt = self.head
        while curr:
            nxt = nxt.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev
    
    #Swapping two nodes in a linked list. Assuming values are all unique
    def swap(self, value1, value2):
        if value1 == value2:
            return
        curr1 = self.head
        prev1 = None
        while curr1 and curr1.value != value1:
            prev1 = curr1
            curr1 = curr1.next
        if not curr1:
            print("Value not in List")
            return

        curr2 = self.head
        prev2 = None
        while curr2 and curr2.value != value2:
            prev2 = curr2
            curr2 = curr2.next
        if not curr2:
            print("Value not in List")
            return

        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2

        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1

        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp

    #Sorting a linked list on ascending values/numbers
    def sort_number(self):
        curr = self.head
        arr = []
        if self.get_length() == 0 or self.get_length() == 1:
            return
        while curr:
            arr.append(curr.value)
            curr = curr.next
        arr.sort()
        self.head = Node(arr[0])
        arr.pop(0)
        for x in arr:
            self.append(Node(x))

    #Merge two sorted linked lists. Assume current linked list is sorted
    def merge_sorted_lists(self, lst):
        current = self.head
        ptr1 = self.head
        ptr2 = lst.head
        if ptr1.value <= ptr2.value:
            self.head = ptr1
            current = ptr1
            ptr1 = ptr1.next
        else:
            self.head = ptr2
            current = ptr2
            ptr2 = ptr2.next
        while ptr1 and ptr2:
            if ptr1.value <= ptr2.value:
                current.next = ptr1
                current = current.next
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                current = current.next
                ptr2 = ptr2.next

        if not ptr1:
            current.next = ptr2
        if not ptr2:
            current.next = ptr1

    #Remove all duplicates in linked list
    def remove_all_duplicates(self):
        ptr1 = self.head
        while ptr1:
            ptr2 = ptr1.next
            prev = ptr1
            while ptr2:
                if ptr2.value == ptr1.value:
                    prev.next = ptr2.next
                    ptr2 = prev.next
                else:
                    prev = ptr2
                    ptr2 = ptr2.next
            ptr1 = ptr1.next

    #Rotate linked list on specific node/value. Assuming all unique values
    def rotate(self, value):
        temp = self.head
        curr = self.head
        prev = None
        while curr and curr.value != value:
            prev = curr
            curr = curr.next
        if curr.next:
            prev = curr
            curr = curr.next

            prev.next = None
            self.head = curr
            while curr.next:
                curr = curr.next
            curr.next = temp
        
#Compare two linked lists to see if they are equal
def compare(lst1, lst2):
    curr1 = lst1.head
    curr2 = lst2.head
    if lst1.get_length() != lst2.get_length():
        return False
    while curr1:
        if curr1.value != curr2.value:
            return False
        else:
            curr1 = curr1.next
            curr2 = curr2.next
    return True



    
    

            

        

    
lst = SLL()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
lst.append(5)
lst.append(6)

lst1 = SLL()
lst1.append(1)
lst1.append(6)
lst1.append(2)
lst1.append(3)
lst1.append(4)
lst1.append(5)



print(compare(lst1, lst))