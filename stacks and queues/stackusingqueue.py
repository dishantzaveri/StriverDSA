from queue import Queue

class QStack: 
    def __init__(self):
        self.q= Queue()
    
    def push(self,x):
        s=self.q.qsize()
        self.q.put(x) 
        for _ in range(s):
            self.q.put(self.q.get())
    
    def pop(self):
        n = self.q.queue[0]
        self.q.get()
        return n
    
    def top(self):
        return self.q.queue[0]
    
    def isEmpty(self):
        return self.q.empty()
    
