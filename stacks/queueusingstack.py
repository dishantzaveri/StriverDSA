class SQueue:
    def __init__(self):
        self.st1=[]
        self.st2=[]
        
    def push(self,x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())
            
    def pop(self):
        if not self.st1:
            return -1
        return self.t1.pop()
    
    def peek(self):
        if not self.st1:
            return -1
        return self.st1[-1]
    
    def isEmpty(self):
        return len(self.st1) ==0