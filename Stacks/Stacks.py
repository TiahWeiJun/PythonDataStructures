import sys
import copy

sys.path.insert(1, '/Users/Admin/Documents/Projects/DSA/Nodes')


from Nodes import Node

class Stack:
    def __init__(self, limit):
        self.top = None
        self.size = 0
        self.limit = limit

    #Visual representation of stack 
    def visual(self):
        string = ''
        duplicate = copy.copy(self)
        for x in range(duplicate.size):
            string += str(duplicate.pop()) 
            string += '\n'
        print(string)



    #Adding to top of stack
    def push(self, Node):
        if self.limit > self.size:
            Node.set_next_node(self.top)
            self.top = Node
            self.size += 1
        else:
            print("Stack Overflow!")

    #Removing and getting value from top of stack
    def pop(self):
        if self.size != 0:
            node_to_remove = self.top
            self.top = self.top.get_next_node()
            self.size -= 1
            return node_to_remove
        else:
            print("Stack Underflow!")
    
    #Getting top value of stack
    def peek(self):
        if self.size != 0:
            return self.top
        else:
            print("Stack Underflow!")
    
    #Creating a reversed stack
    def reverse(self):
        newStack = Stack(100)
        for x in range(self.size):
            node = self.pop()
            newStack.push(node)
        return newStack

    #Getting Max value from Stack:
    def get_max(self):
        if self.size == 0:
            return None
        else:
            lst = []
            for x in range(self.size):
                value = self.pop().get_value()
                lst.append(value)
            return max(lst)
            


#Reversing a string using stack
def reverse_string(string):
    stack = Stack(100)
    for item in string:
        stack.push(Node(item))
    newstring = ''
    for item in string:
        x = stack.pop().get_value()
        newstring += x
    return newstring

#Converting integer value to Binary values
def int_to_bin(num):
    stack = Stack(100)
    while num > 0:
        remainder = num%2
        stack.push(Node(remainder))
        num = num//2
    string = ''
    for x in range(stack.size):
        binary_value = stack.pop().get_value()
        string += str(binary_value)
    return string

#Determine if parantheses in a string are balanced
def pair_of_paran(x, y):
    if x == '{' and y == '}':
        return True
    elif x == '[' and y == ']':
        return True
    elif x == '(' and y == ')':
        return True
    else:
        return False
    

def balanced_paran(string):
    stack = Stack(500)
    index = 0
    is_balanced = True

    while index<len(string) and is_balanced:
        char = string[index]
        if char in "({[":
            stack.push(Node(char))
            
        elif char in "}])":
            if stack.size == 0:
                is_balanced = False
            else:
                value = stack.pop().get_value()
                if not pair_of_paran(value, char):  
                    is_balanced = False
        index += 1
        

    if stack.size == 0 and is_balanced:
        return True
    else: 
        return False


a1 = Node(1)
a2 = Node(2)
a3 = Node(3)
a4 = Node(4)

s = Stack(100)
print(s.get_max())




