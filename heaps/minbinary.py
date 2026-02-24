class BinaryHeap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0]*capacity
    def parent(self,i):
        return (i-1)//2
    def left(self,i):
        return 2*i+1
    def right(self,i):
        return 2*i+2
    def insert(self,x):
        if self.size == self.capacity:
            print('overflow bruh')
            return
        self.arr[self.size] = x
        k = self.size
        self.size +=1
        
        while k!= 0 and self.arr[self.parent(k)>self.arr[k]]:
            self.arr[self.parent(k)],self.arr[k]=self.arr[k],self.arr[self.parent(k)]
    def heapify(self,ind):
        li = self.left(ind)
        ri = self.right(ind)
        smallest = ind
    
        if li < self.size and self.arr[li] < self.arr[smallest]:
            smallest = li
        if ri < self.size and self.arr[ri] < self.arr[smallest]:
            smallest = ri
        if smallest != ind:
            self.arr[ind], self.arr[smallest] = self.arr[smallest],self.arr[ind]
            self.heapify(smallest)
        
    