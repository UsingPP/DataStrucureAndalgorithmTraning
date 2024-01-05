
from inspect import stack


class ArrayStack :
    def __init__(self, capacity = 10) :
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self) :
        if self.top == -1 :
            return True
        return False

    def isFull(self) :
        return self.top == self.capacity

    def push(self, item) :
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else :
            print("ERROR::StackOverflow")

    def pop(self) :
        if not self.isEmpty() :
            item = self.array[self.top]
            self.top -= 1
            return item
        else :
            print("ERROR::StackUnderflow")
        
    def peek(self) :
        if not self.isEmpty() :
            return self.array[self.top]
        else :
            print("ERROR::StackUnderflow")

    def size(self) :
        return self.top+1

    def clear(self) :
        self.top = -1

    def display(self) :
        if not self.isEmpty() :
            serch = 0
            while (serch <= self.top) :
                print(self.array[serch], end = ", ")
                serch += 1
            
        else :
            print("스택에 아무것도 없습니다")


def checkBrackets(statement) :
    checkStack = ArrayStack(100)
    for ch in statement:
        if ch in ("(","{","[") :
            checkStack.push(ch)
        elif ch in (')','}', ']') :
            if checkStack.isEmpty() :
                return False
            else :
                left = checkStack.pop()

                if (ch == '}' and left != '{' ) or (ch == ']' and left != '[') and (ch == ')' and left != '(') :
                    return False

    return checkStack.isEmpty()
