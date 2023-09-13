import sys
input = sys.stdin.readline

class Node:
    val = None
    left = None
    right = None
    
    def __init__(self, val):
        self.val = val

        
def find(node, value):
    if node is None:
        return None
    
    if node.val == value:
        return node
    
    left_result = find(node.left, value)
    if left_result:
        return left_result
    
    right_result = find(node.right, value)
    if right_result:
        return right_result
    

def preOrder(head):
    if head is not None:
        print(head.val, end="")
        preOrder(head.left)
        preOrder(head.right)

def inOrder(head):
    if head is not None:
        inOrder(head.left)
        print(head.val, end="")
        inOrder(head.right)
        
def postOrder(head):
    if head is not None:
        postOrder(head.left)
        postOrder(head.right)
        print(head.val, end="")
    
    
if __name__ == "__main__":
    n = int(input())
    
    start = list(input().split())
    head = Node(start[0])
    if (start[1] != '.'): head.left = Node(start[1])
    if (start[2] != '.'): head.right = Node(start[2])
    
    for i in range(n-1):
        sysin = list(input().split())
        locNode = find(head, sysin[0])
        
        if locNode is not None:
            if sysin[1] != '.':
                locNode.left = Node(sysin[1])
            if sysin[2] != '.':
                locNode.right = Node(sysin[2])
    
    preOrder(head)
    print()
    inOrder(head)
    print()
    postOrder(head)