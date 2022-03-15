class stack:
    def __init__(self):
        self.stack_size = 1000
        self.stack = []

    def GetStackLenght(self):
        return len(self.stack)

    def push(self, value):
        if (self.GetStackLenght() + 1) > self.stack_size:
            raise Exception("Error: Stack Overflow.")
        self.stack.append(value)
        return self.stack
    
    def pop(self):
        if (self.GetStackLenght())  == 0:
            raise Exception("Error: Stack Underflow.")
        #value = self.stack[-1]
        del self.stack[-1]
        return self.stack
