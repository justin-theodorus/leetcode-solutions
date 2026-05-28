class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n


    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1


    def popback(self) -> int:
        
        #self.arr[self.length] = -1
        if self.length > 0:
            self.length -= 1
        tmp = self.arr[self.length]
        return tmp

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new = [0] * self.capacity

        for i in range(self.length):
            new[i] = self.arr[i]
        self.arr = new

    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
