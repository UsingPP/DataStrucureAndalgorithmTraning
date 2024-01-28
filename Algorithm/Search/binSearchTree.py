import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from Tree import binarytree

class BTSNode :
    def __init__(self, key, data) :
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) :
        return f"({self.key}:{self.data})"

# 이진탐색트리
def select_bts_option(root, param, option) :
    if option == "key" :
        return search_bst(root, param)
    elif option == "data" :
        return search_data_bst(root, param)
    else :
        return None

def search_bst(root, key) :
    if root == None :
        return None
    elif key == root.key :
        return root
    elif key < root.key :
        return search_bst(root.left, key)
    elif key > root.key :
        return search_bst(root.right, key)
    

def search_data_bst(root, data) :
    if root == None :
        return None
    elif root.data == data :
        return root
    res = search_data_bst(root.left, data)
    if res is not None :
        return res
    
    else : return search_data_bst(root.right, data)


def insert_bts(root, node) :
    if root == None :
        return node
    
    if node.key == root.key :
        return root
    
    if node.key < root.key :
        root.left = insert_bts(root.left, node)
    
    elif node.key > root.key :
        root.right = insert_bts(root.right, node)
    
    return root

def delete_node(root, key) :
    if root == None:
        return root
    
    if key < root.key :
        root.left = delete_node(root.left, key)

    elif key > root.key :
        root.right = delete_node(root.right, key)

    else :
        if root.left == None :
            return root.right
        
        if root.right == None :
            return root.left
        
        succ = root.right
        while succ.left != None:
            succ = succ.left

        root.key = succ.key
        root.data = succ.data
        root.right = delete_node(root.right, succ.key)

    return root




def print_node(msg, n) :
    print(msg, n if n != None else "탐색 실패")

def print_tree(msg, r) :
    print(msg, end=" ")
    binarytree.preorder(r)
    print()

data = [(6, "여섯"), ( 8,"여덣"),( 2, "둘"),(4,"넷" ),( 7,"일곱" ),( 5,"다섯" ),(1 ,"하나" ), (9 , "아홉"), (3, "셋"),(0 , "영")]
root = None
for i in range(0, len(data)) :
    root = insert_bts(root, BTSNode(data[i][0], data[i][1]))

print_tree("최초 :", root)

n = search_bst(root, 3); print_node("serch 3: ", n)
n = search_bst(root, 8); print_node("serch 8: ", n)
n = search_bst(root, 0); print_node("serch 0: ", n)
n = search_bst(root, 10); print_node("serch 10: ", n)
n = search_data_bst(root, "둘"); print_node("serch 둘: ", n)
n = search_data_bst(root, "열"); print_node("serch :열 ", n)
n = search_bst(root, 3); print_node("serch : ", n)

root = delete_node(root, 7); print_tree("del 7: ", root)
root = delete_node(root, 8); print_tree("del 8: ", root)
root = delete_node(root, 2); print_tree("del 2: ", root)
root = delete_node(root, 6); print_tree("del 6: ", root)