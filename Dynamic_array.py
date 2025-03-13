#This class creates a resizeable or dynamic array similar to the ArrayList
#in java, it contains some methods to ensure that the array is resizeable
class DynamicArray:

    #The DynamicArray constructor that initializes the array, the size
    #of the array and the capacity of the array
    def __init__(self, capacity: int):
        self.size = 0 #number of elements in the array
        self.capacity = capacity
        self.dynamic_arr = [None]*self.capacity #instantiate an array

    #If the element is in a valid range return it.
    def get(self, i: int) -> int:
        if i >= 0 and i < self.size:
            return self.dynamic_arr[i]
        else:
            raise Exception("Element not found")


    #Assign a value to an index in the array.
    def set(self, i: int, n: int) -> None:
        if i >= 0 and i < self.size:
           self.dynamic_arr[i] = n
        else:
            raise Exception("Element index out of scope")

    #Pushes the value of n to the end of the array, without holes
    def pushback(self, n: int) -> None:
        if self.size == self.capacity: #resize if the array is full
            self.resize()
        self.dynamic_arr[self.size] = n
        self.size += 1 #update the number of elements in the array

    #Soft-pop the element at the end of the array and return the value
    def softPopback(self) -> int:
        self.size -=1
        return self.dynamic_arr[self.size]

    #deletes the element at index, take all the elements after index
    #, shift them backward one space and returns the value at index
    def popback(self, index:int) -> int:
        value = self.dynamic_arr[index]
        for i in range (index, self.size-1):
            self.dynamic_arr[i] = self.dynamic_arr[i+1]
        self.size -=1
        return value

    #Make a new array that has two times the capacity of the original array
    #then copy the contents of the old array into the new array
    #and assign the new array to the old array.
    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None]* self.capacity

        # copy elements to new_arr
        for i in range (self.size):
            new_arr[i]= self.dynamic_arr[i]
        self.dynamic_arr =new_arr

    #Returns the number of elements in the array
    def getSize(self) -> int:
        return self.size

    #Returns the capacity of the array
    def getCapacity(self) -> int:
        return self.capacity
