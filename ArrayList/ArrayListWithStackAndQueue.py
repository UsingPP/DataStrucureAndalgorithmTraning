import ArrayList

class ListStack :
    def __init__(self) :
        self.top = None
        self.count = 0

    def isEmpty(self) :
        return self.top == None

    def isFull(self) :
        return False
    
    def getNode(self, pos) :
        if pos < 0 : return None
        ptr = self.top
        for i in range(pos) :
            if ptr is None : return None
            ptr = ptr.link
        return ptr

    def push(self, elem) :
        node = ArrayList.Node(elem)
        if self.top is None :
            self.top = node
        else :
            node.link = self.top
            self.top = node
        self.count += 1

    def pop(self) :
        if self.isEmpty() :
            return None
        self.count -= 1
        elem = self.top.data
        self.top = self.top.link
        return elem

            
    def peek(self) :
        return self.top.data

    def size(self) :
        return self.count

    def clear(self) :
        self.top = None

    def display(self, msg = "Stack::[ ") :
       ptr = self.top
       print(msg, end = "")
       self.Display(ptr)
       print("]")

    def Display(self, ptr) :
        if ptr == None :
            pass
        else :
            demp = ptr
            ptr = ptr.link
            self.Display(ptr)
            print(demp.data, end = " ")

class ListQueue :
    def __init__(self) :
        self.head = None
        self.count = -1

    def isEmpty(self) :        return self.head == None
    
    def isFull(self) :        return False

    def getNode(self, pos) :
        if pos < 0 : return None
        ptr = self.head
        for i in range(pos) :
            if ptr is None : return None
            ptr = ptr.link
        return ptr

    def enqueue(self, elem) :
        node = ArrayList.Node(elem)
        if self.head is None :
            self.head = node
        else :
            node.link = self.head
            self.head = node
        self.count += 1

    def dequeue(self) :
        elem = None
        if self.isEmpty():
            self.count -= 1
            return elem
        before = self.getNode(self.count - 1)
        self.count -= 1
        if before is None :
            elem = self.head.data
            self.head = self.head.link
            return elem
        else : 
            elem = before.popNext()
            return elem.data

    def display(self, msg = "Queue::[ ") :
       ptr = self.head
       print(msg, end = "")
       self.Display(ptr)
       print("]")

    def Display(self, ptr) :
        if ptr == None :
            pass
        else :
            demp = ptr
            ptr = ptr.link
            self.Display(ptr)
            print(demp.data, end = " ")

    def size(self) :
        return self.count + 1