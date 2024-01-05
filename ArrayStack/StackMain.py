import ArrayStack

a = ArrayStack.ArrayStack(100)

msg = "안녕하세요. 반갑습니다"

for c in msg :
    a.push(c)

a.display()

while not a.isEmpty() :
    print(a.pop(), end= "")

print()
print("================")
print()

test_1 = "{A[(3 + 4)] - 2}"
test_2 = "if ((X<3) and (Y=2)"

print(ArrayStack.checkBrackets(test_1))
print(ArrayStack.checkBrackets(test_2))

print()
print("================")
print()
