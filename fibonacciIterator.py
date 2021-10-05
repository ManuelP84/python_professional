import time

class Fibonacci_Iterator():

    def __init__(self, max= None):
        self.max = max
    
    def __iter__(self):
        self.num_0 = 0
        self.num_1 = 1
        self.counter = 0
        return self

    def __next__(self):
        if  self.counter ==0:
            self.counter+=1
            return 0
        elif self.counter== 1:
            self.counter+=1
            return 1
        else:
            self.next = self.num_0 + self.num_1
            #self.num_0 = self.num_1  --> Changed by swaping. See line 25
            #self.num_1 = self.next   --> Changed by swaping. See line 25
            self.num_0, self.num_1 = self.num_1, self.next  # Swaping
            self.counter+=1
            if not self.max:
                return self.next
            elif self.counter<=self.max:
                return self.next
            else:
                raise StopIteration

if __name__ == "__main__":
    Fibonacci = Fibonacci_Iterator(4)
    for element in Fibonacci:
        print(element)
        time.sleep(1)
