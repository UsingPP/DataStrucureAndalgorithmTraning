from binarytree import *


#TREE SEARCHING TEST
d = BTNode('D', None, None)
e = BTNode('E', None, None)
b = BTNode('B', d, e)
f = BTNode('F', None, None)
c = BTNode('C', f, None)
root = BTNode('A', b, c)

print('\n In-Order : ', end = ""); inorder(root)
print('\n Pre-Order : ', end = ""); preorder(root)
print('\n Post-Order : ', end = ""); postorder(root)
print('\n Level-Order : ', end = ""); levelorder(root)
print()

print("노드의 개수 = %d개" % count_node(root))
print("트리의 높이 = %d" % calc_height(root))




#ENCODING TREE TEST
morseCodeTree = make_morse_tree()

inorder(morseCodeTree)
print()

str = "HELLO"
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("Morse Code is : ", mlist)
print("Decodeing : ", end = "")
for code in mlist :
    ch = decoding(morseCodeTree, table)
    print(ch, end = " ")
print()

#EVAL TREE TEST
str = "1 3 + 4 2 / *"
expr = str.split()
print("토큰 분리 :", expr)
root = buildETree(expr)
print('\n In-Order : ', end = ""); inorder(root)
print('\n Pre-Order : ', end = ""); preorder(root)
print('\n Post-Order : ', end = ""); postorder(root)
print('\n EVALUATE : ', end = ""); print(evaluate(root))

