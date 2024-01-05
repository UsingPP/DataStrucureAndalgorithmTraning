import ArrayQueue
import random

q = ArrayQueue.ArrayQueue(10)

q.display("초기상태")
while(not q.isFull()) :
    i = random.randint(0,100)
    q.enqueue(i)
q.display("포화상태")

q.display("삭제 순서 : ")
while(not q.isEmpty()) :
    print(q.dequeue(), end = " ")
print()

q2 = ArrayQueue.ArrayQueue(6)

q2.display("초기상태 ")
while(not q2.isFull()) :
    i = random.randint(0,100)
    q2.enqueue(i)
q2.display("포화상태")

print("q2에 추가로 숫자 2개 삽입")

q2.enqueue(1)
q2.enqueue(2)
q2.display("일반 enqueue의 경우")

q2.ringEnqueue(1)
q2.ringEnqueue(2)
q2.display("ring enqueue의 경우")

dq = ArrayQueue.CircularDeque(10)

for i in range(9) :
    if i%2 == 0 :
        dq.addFront(i)
    else :
        dq.addRear(i)

dq.display("dq :")


print("=======큐를 이용한 피보나치 연습========")
for i in range(1, 10) :
    print(ArrayQueue.fiboCalc(i))

