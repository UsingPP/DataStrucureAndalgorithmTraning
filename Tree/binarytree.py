import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ArrayQueue import ArrayQueue

table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]


class BTNode :
    def __init__(self, elem, left = None, right = None) :
        self.data = elem
        self.left = left
        self.right = right
        
    def isLeaf(self) :
        return (self.left == None) and (self.right == None)
        
def preorder (n) :
    if n is not None :
        print(n.data, end = " ")
        preorder(n.left)
        preorder(n.right)
        
def inorder (n) :
    if n is not None :
        inorder(n.left)
        print(n.data, end = " ")
        inorder(n.right)
        
def postorder (n) :
    if n is not None :
        postorder(n.left)
        postorder(n.right)
        print(n.data, end = " ")
    
def levelorder(root) :
    queue = ArrayQueue.ArrayQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None:
            print(n.data, end = "")
            queue.enqueue(n.left)
            queue.enqueue(n.right)
            
def count_node(n) :
    if n is None :
        return 0
    else : return count_node(n.left) + count_node(n.right) + 1
    
def calc_height(n) :
    if n is None :
        return 0
    else :
        hLeft =  calc_height(n.left)
        hRight = calc_height(n.right)
        if (hLeft > hRight) :
            return hLeft + 1
        else :
            return hRight + 1
        
def encode(ch) :
    idx = ord(ch)-ord('A')
    return table[idx][1]

def decode_simple(morse):
    for tp in table:
        if morse == tp[1] :
            return tp[0]
        
def make_morse_tree() :
    root = BTNode(None, None, None)
    for tp in table :
        code = tp[1]
        node = root
        for c in code :
            if c == '.' :
                if node.left == None :
                    node.left = BTNode(None, None, None)
                node = node.left
            elif c == "-" :
                if node.right == None :
                    node.right = BTNode(None)
                node = node.right
        node.data = tp[0]
            
    return root

def decoding(root, code) :
    node = root
    for c in code :
        if c == '.' : node = node.left
        elif c== '-' :node = node.right
    return node.data


def evaluate(node) :
    if node is None :
        return 0
    elif node.isLeaf() :
        return node.data
    else :
        op1 = evaluate(node.left)
        op2 = evaluate(node.right)
        if node.data == '+' : return op1 + op2
        elif node.data == '-' : return op1 - op2
        elif node.data == '*' : return op1 * op2
        elif node.data == '/' : return op1 / op2
        
        
def buildETree(expr) :
    if len(expr) == 0 :
        return None
    
    token = expr.pop()
    if token in "+-*/" :
        node = BTNode(token)
        node.right = buildETree(expr)
        node.left = buildETree(expr)
        return node
    else :
        return BTNode(float(token))