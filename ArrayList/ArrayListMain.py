import ArrayListWithStackAndQueue
import ArrayList
import random

s = ArrayList.LinkedList()
s.display()
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display("LinkedList 삽입 5회 : ")
s.replace(2, 90)
s.display("LinkedList 교체 1회 : ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("LinkedList 삭제 3회 : ")


s = ArrayList.DoubleLinkedList()
s.display()
s.insert(0,10)
s.insert(0,20)
s.insert(1,30)
s.insert(s.size(),40)
s.insert(2,50)
s.display("DoubleLinkedList 삽입 5회 : ")
s.replace(2, 90)
s.display("DoubleLinkedList 교체 1회 : ")
s.delete(2)
s.delete(3)
s.delete(0)
s.display("DoubleLinkedList 삭제 3회 : ")

newStack = ArrayListWithStackAndQueue.ListStack()

newStack.display()

for i in range(10) :
    num = i + 10 + random.randint(1, 10)
    print(num, end = " ")
    newStack.push(num)

print()
newStack.display()


for i in range(newStack.size()) :
    print(newStack.pop(), end = "   ")
print()
newStack.display()

print();print()
newQueue = ArrayListWithStackAndQueue.ListQueue()
newQueue.display()

for i in range(10) :
    num = i + 10 + random.randint(1, 10)
    print(num, end= " ")
    newQueue.enqueue(num)
print()
newQueue.display()

for i in range(newQueue.size()) :
    print(newQueue.dequeue(), end = " ")

newQueue.display()
