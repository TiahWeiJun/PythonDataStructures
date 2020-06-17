import sys

sys.path.insert(1, '/Users/Admin/Documents/Python Data Structures/Nodes')

from Nodes import Node

class LinkedList:
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

    #Length of linked list
    def get_length(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next_node()
        return count

    #Adding to start of LinkedList
    def prepend(self, Node):
        Node.set_next_node(self.head)
        self.head = Node

    #Adding to end of LinkedList
    def append(self, Node):
        if self.head is None:
            self.head = Node
        else:
            current_node = self.head
            while current_node.get_next_node() is not None:
                current_node = current_node.get_next_node()
            current_node.set_next_node(Node)

    #Adding after a specific Node:
    def add_after_node(self,after_Node,Node_to_add):
        curr = self.head
        next = curr.get_next_node()
        while curr and curr != after_Node:
            curr = curr.get_next_node()
            next = next.get_next_node()
        curr.set_next_node(Node_to_add)
        Node_to_add.set_next_node(next)

                

    #Removing specific Node by value
    def remove(self, Node):
        value_to_remove = Node.get_value()
        if self.head.get_value() == value_to_remove:
            self.head = self.head.get_next_node()
        else:
            current_node = self.head
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else: 
                    current_node = current_node.get_next_node()

    #Removing specific node by position
    def remove_by_index(self, index):
        if index == 0:
            self.head = self.head.get_next_node()
        else:
            current_node = self.head
            previous_node = None
            for x in range(index):
                previous_node = current_node
                current_node = current_node.get_next_node()
            previous_node.set_next_node(current_node.get_next_node())
            
    #Return nth to last node
    def nth_last_node(self, n):
        length = self.get_length()
        if n > length or n == 0:
            return None
        else:
            num_iter = length - n
            curr = self.head
            for x in range(num_iter):
                curr = curr.get_next_node()
            return curr
        

    #Reversing a linked list
    def reverse(self):
        prev = None
        current = self.head
        following = self.head
        while current:
            following = following.get_next_node()
            current.set_next_node(prev) 
            prev = current
            current = following
        self.head = prev
                          
    #Swapping two nodes in a linked list. Assuming nodes are unique
    def swap_nodes(self, Node1, Node2):
        if Node1 == Node2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1 != Node1:
            prev_1 = curr_1
            curr_1 = curr_1.get_next_node()

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2 != Node2:
            prev_2 = curr_2
            curr_2 = curr_2.get_next_node()

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.set_next_node(curr_2)
        else:
            self.head = curr_2

        if prev_2:
            prev_2.set_next_node(curr_1)
        else:
            self.head = curr_1

        following = curr_1.get_next_node()
        curr_1.set_next_node(curr_2.get_next_node())
        curr_2.set_next_node(following)

    #Merge two sorted linked lists
    def merge_sorted_lists(self, lst):
        curr1 = self.head
        curr2 = lst.head
        temp = None

        if curr1.get_value() < curr2.get_value():
            temp = curr1
            curr1 = temp.get_next_node()
        else:
            temp = curr2
            curr2 = temp.get_next_node()
        new_head = temp

        while curr1 and curr2:
            if curr1.get_value() < curr2.get_value():
                temp.set_next_node(curr1)
                temp = curr1
                curr1 = temp.get_next_node()
            else:
                temp.set_next_node(curr2)
                temp = curr2
                curr2 = temp.get_next_node()
        if not curr1:
            temp.set_next_node(curr2)
        if not curr2:
            temp.set_next_node(curr1)
        
        self.head = new_head

    #Removing duplicates
    def remove_duplicate_values(self):
        curr1 = self.head
        while curr1:
            curr2 = curr1.get_next_node()
            prev_node = curr1
            while curr2:
                if curr2.get_value() == curr1.get_value():
                    prev_node.set_next_node(curr2.get_next_node())
                    curr2 = prev_node.get_next_node()
                else:
                    prev_node = curr2
                    curr2 = curr2.get_next_node()
            curr1 = curr1.get_next_node()

    #Count number of Occurences
    def count_occurences(self, value):
        curr = self.head
        count = 0
        while curr: 
            if curr.get_value() == value:
                count += 1
            curr = curr.get_next_node()
        return count

    #Rotate linked list on a specific Node
    def rotate(self, Node):
        temp = self.head
        curr = self.head
        while curr and curr != Node:
            curr = curr.get_next_node()
        if curr.get_next_node():
            next = curr.get_next_node()
            self.head = next
            curr.set_next_node(None)
            while next and next.get_next_node():
                next = next.get_next_node()
            next.set_next_node(temp)

    #Move tail node to head node
    def tail_to_head(self):
        #temp = self.head
        curr = self.head
        prev = None
        while curr and curr.get_next_node():
            prev = curr
            curr = curr.get_next_node()
        curr.set_next_node(self.head.get_next_node())
        prev.set_next_node(self.head)
        self.head.set_next_node(None)
        self.head = curr
    
    #Sum of two numbers using linked list
    def sum_two_lists(self, lst):
        curr1 = self.head
        curr2 = lst.head

        newlst = LinkedList()
        carry = 0
        while curr1 or curr2:
            if not curr1:
                x = 0
            else:
                x = curr1.get_value()
            if not curr2:
                y = 0
            else:
                y = curr2.get_value()
            sum = x + y + carry
            if sum >= 10:
                carry = 1
                newlst.append(Node(sum%10))
            else:
                carry = 0
                newlst.append(Node(sum))
            if curr1:
                curr1 = curr1.get_next_node()
            if curr2: 
                curr2 = curr2.get_next_node()
        return newlst.visual()
        

#Determine if a linked list is a palindrome
def is_palindrome(lst):
    if lst.get_length() == 0 or lst.get_length() == 1:
        return True
    curr = lst.head
    string = ""
    while curr:
        str_value = str(curr.get_value())
        string += str_value
        curr = curr.get_next_node()
    return string == string[::-1]


a1 = Node(1)
a2 = Node(2)
print(a2)
lst = LinkedList()
lst.append(a1)
lst.append(a2)
lst.visual()

