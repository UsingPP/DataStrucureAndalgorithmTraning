
class Node :
    def __init__(self, elem, link = None) :
        self.data = elem
        self.link = link
    
    def append(self, node) :
        if node is not None :
            node.link = self.link
            self.link = node
    
    def popNext (self) :
        next = self.link
        if next is not None :
            self.link = next.link
        return next

class LinkedList :
    def __init__(self) :
        self.head = None

    def isEmpty(self) :
        return self.head == None
    def isFull(self) :
        return False
    
    def getNode(self, pos) :
        if pos < 0 : return None
        ptr = self.head
        for i in range(pos) :
            if ptr.link == None :
                return None
            ptr = ptr.link
        return ptr
    
    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node is None : return None
        return node.data
    
    def insert(self, pos, elem) :
        node = Node(elem)
        before = self.getNode(pos-1)
        if before == None :
            node.link = self.head
            self.head = node
        else : before.append(node)
    
    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :
            before = self.head
            if before is not None :
                self.head = self.head.link
            return before
        else : return before.popNext()

    def replace(self, pos, elem) :
        ptr = self.getNode(pos)
        if ptr == None : return ptr
        else : 
            ptr.data = elem
            return ptr.data
        

    def size(self) :
        counter = 0
        ptr = self.head
        while ptr is not None :
            counter += 1
            ptr = ptr.link
        return counter
    
    def display(self, msg = "Linked_List: ") :
        print(msg, end = '')
        ptr = self.head
        while ptr is not None :
            print(ptr.data, end = "->")
            ptr = ptr.link
        print('None')

class DNode :
    def __init__(self, elem, prev = None, next = None) :
        self.data = elem
        self.prev = prev
        self.next = next

    def append(self, node) :
        node.prev = self
        node.next = self.next
        if node.next is not None :
            node.next.prev = node
        self.next = node


    def popNext(self) :
        node = self.next
        if node is not None :
            self.next = node.next
            if self.next is not None :
                node.next.prev = self
        return node
    
class DoubleLinkedList :
    def __init__(self) :
        self.head = None

    def isEmpty(self) :
        return self.head == None
    def isFull(self) :
        return False
    
    def getNode(self, pos) :
        if pos < 0 : return None
        ptr = self.head
        for i in range(pos) :
            if ptr.next == None :
                return None
            ptr = ptr.next
        return ptr
    
    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node is None : return None
        return node.data

    def size(self) :
        counter = 0
        ptr = self.head
        while ptr is not None :
            counter += 1
            ptr = ptr.next
        return counter
    
    def display(self, msg = "Linked_List: ") :
        print(msg, end = '')
        ptr = self.head
        while ptr is not None :
            print(ptr.data, end = "->")
            ptr = ptr.next
        print('None')

    def insert(self, pos, elem) :
        node = DNode(elem)
        before = self.getNode(pos-1)
        if before is None :
            node.next = self.head
            if node.next is not None :
                node.next.prev = node
            self.head = node
        else : before.append(node)

    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before is None :
            before = self.head
            if self.head is not None :
                self.head = self.head.next
            if self.head is not None :
                self.head.prev = None
            return before
        else : return before.popNext()

    def replace(self, pos, elem) :
        ptr = self.getNode(pos)
        if ptr == None : return ptr
        else : 
            ptr.data = elem
            return ptr.data