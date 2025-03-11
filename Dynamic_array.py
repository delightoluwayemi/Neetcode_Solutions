class DynamicArray:

    def __init__(self, capacity: int):
        self.size = 0 #number of elements in the array
        self.capacity = capacity
        self.dynamic_arr = [None]*self.capacity #instantiate an array

    def get(self, i: int) -> int:
        return self.dynamic_arr[i]

    def set(self, i: int, n: int) -> None:
        self.dynamic_arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.dynamic_arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -=1
        return self.dynamic_arr[self.size]

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [None]* self.capacity

        # copy elements to new_arr
        for i in range (self.size):
            new_arr[i]= self.dynamic_arr[i]
        self.dynamic_arr =new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
