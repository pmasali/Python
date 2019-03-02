# Python program to convert Infix to Postfix

# Class to convert the expression
class conversion:

    #construct class variables
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        # This array is used to stack
        self.array = []
        # precedence setting
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    #check if stack is empty
    def isEmpty(self):
        return True if self.top == -1 else False
    
    #return the value of top of stack
    def peek(self):
        return self.array[-1]
    
    #Pop the element from stack
    def pop(self):
        if not self.isEmpty:
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    
    # Push the element to the stack
    def push(self, op):
        self.top += 1
        self.array.append(op)
    
