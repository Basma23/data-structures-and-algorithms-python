from data_structures_and_algorithms.data_structures.tree.tree import Node, BinaryTree

def find_maximum_value(root):
    if root == None:  
        return float('-inf') 
    res = root.value 
    lres = find_maximum_value(root.left)  
    rres = find_maximum_value(root.right)  
    if (lres > res): 
        res = lres  
    if (rres > res):  
        res = rres  
    return res 

if __name__ == '__main__': 
    root = Node(7)
    root.left = Node(7)
    root.right = Node(5)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.left.right.left = Node(5)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)
  
    print("Maximum element is", find_maximum_value(root)) 