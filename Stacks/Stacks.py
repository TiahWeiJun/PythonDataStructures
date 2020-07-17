class Stack:
    def __init__(self, limit = 100):
        self.list = []
        self.limit = limit

    def __repr__(self):
        newlst = self.list[::-1]
        string = ''
        for x in newlst:
            string += "{}".format(x)
            string += "\n"
        return string

    #Adding to top of stack
    def push(self, value):
        if len(self.list) < self.limit:
            self.list.append(value)
        else:
            print("Stack is full")

    #Removing and getting value from top of stack
    def pop(self):
        if len(self.list) > 0:
            value = self.list.pop(-1)
            return value
        else:
            print("Stack is empty")

    #Getting top value of stack
    def peek(self):
        if len(self.list) > 0:
            value = self.list[-1]
            return value
        else:
            print("Stack is empty")

    #Reversing a stack
    def reverse(self):
        self.list = self.list[::-1]


#Reversing string using a stack
def reverse_string(string):
    stk = Stack()
    for item in string:
        stk.push(item)
    newstring = ''
    for i in range(len(string)):
        newstring += stk.pop()
    return newstring

#Convert integer to binary
def int_to_binary(num):
    stk = Stack()
    while num != 0:
        if num % 2 == 0:
            stk.push(0)
        elif num % 2 == 1:
            stk.push(1)
        num = num // 2
    string = ''
    for x in range(len(stk.list)):
        string += str(stk.pop())
    return string
    
#Determine if parantheses in a string are balanced
def balanced_paran(string):
    newstr = string.replace(" ", "")
    stk = Stack()
    for item in newstr:
        if item in ["}", ")" , "]"]:
            if len(stk.list) == 0:
                return False
            else:
                value = stk.pop()
                if not parans_match(value, item):
                    return False
        elif item in ["{", "(" , "["]:
            stk.push(item)
           
    if len(stk.list) == 0:
        return True
    else:
        return False


def parans_match(open, close):
    if (open == "(" and close == ")") or (open == "{" and close == "}") or (open == "[" and close == "]"):
        return True
    else:
        return False

def test():
    for i in range(6, -1, -1):
            print(i)

test()


