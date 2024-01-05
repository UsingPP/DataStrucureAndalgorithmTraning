class ArrayQueue :
    def __init__(self, capacity = 10) :
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.array = [None]*self.capacity


    def isEmpty(self) :
        return self.front == self.rear

    def isFull(self) :
        return self.front == (self.rear+1)%self.capacity
    
    def enqueue(self, item) :
        if not self.isFull() :
            self.array[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            return True
        return False
    
    def ringEnqueue(self, item) : #링 버퍼
        self.array[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        if self.isEmpty() : #꽉 찬 큐에 새로 삽입 시 큐의 front == rear
            self.front = (self.front + 1) % self.capacity

    def dequeue(self) :
        if not self.isEmpty() :
            item = self.array[self.front]
            self.front = (self.front+1) % self.capacity
            return item
        else : return False

    def peek(self) :
        if not self.isEmpty() :
            return self.array[(self.front+1) % self.capacity]
        
    def size (self) :
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self, msg) :
        print(msg, end = ' [')
        for i in range(self.front, self.front + self.size()) :
            print(self.array[i%self.capacity], end = " ")
        print("]")
    
class CircularDeque(ArrayQueue) :
    def __init__(self, capacity) :
        super().__init__(capacity)

    def addFront(self, item) :
        if not self.isFull() :
            self.front = (self.front-1 + self.capacity) % self.capacity
            self.array[self.front] = item
        else : return False
            

    def addRear(self, item) :
        self.enqueue(item)

    def deleteRear(self) :
        return self.dequeue()
    
    def deleteFront(self) :
        if not self.isEmpty() :
            item = self.array[self.front]
            self.front = (self.front + 1) % self.capacity
            return item
        else : return False
    
    def getFront(self) :
        return self.peek()
    
    def getRear(self) :
        if not self.isEmpty() :
            return self.array[self.rear]
        else : return False


def fiboCalc(num) :
    if num == 1 : return 1
    elif num == 2 : return 1

    que = ArrayQueue(3)
    que.enqueue(1); que.enqueue(1)
    for _ in range(num-2) :
        first = que.dequeue(); sec = que.dequeue()
        que.enqueue(first + sec)
        que.enqueue(first)

    return que.dequeue()