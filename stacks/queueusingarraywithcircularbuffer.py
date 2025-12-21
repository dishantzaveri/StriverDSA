class ArrayQueue:
    def __init__(self):
        self.arr=[0]*10
        self.start=-1
        self.end=-1
        self.currSize = 0
        self.maxSize = 10
        
    def push(self,x):
        if self.currSize == self.maxSize:
            return
        if self.end==-1:
            self.start = self.end = 0
        else:
            self.end=(self.end +1) % self.maxSize
        self.arr[self.end] = x
        self.currSize +=1
    
    def pop(self):
        if self.start == -1:
            return None
        val = self.arr[self.start]
        if self.currSize ==1:
            self.start = self.end = -1
        else:
            self.start = (self.start +1) % self.maxSize
        self.currSize -=1
        return val
    
    def peek(self):
        if self.start == -1:
            return None
        return self.arr[self.start]
    
    def isEmpty(self):
        return self.currSize==0
    
    