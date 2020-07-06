## Two trees are considered "leaf-similar" if the order of their leaves is the same from left to right.
## This function uses DFS to check if two given trees are "leaf-similar".

class Node:
    def __init__(self, val, visited):
        self.val = val
        self.visited = visited
        self.left = None
        self.right = None

# global variables "leaves" is used since leafSimilar is recursive.
leaves = []

# This uses DFS instead of BFS since we're looking to match the leaves 
# in exact left to right order. 
def leafSimilar(root):
    global leaves

    if root == None:
        return ""

    stack = [root]
    root.visited = True

    if root.left == None and root.right == None:
        leaves.append(root.val)
    
    else:
        if root.left != None:
            stack.append(root.left)
        if root.right != None:
            stack.append(root.right)

    for node in stack:
        if node.visited == False:
            node.visited = True
            leafSimilar(node)


if __name__ == "__main__":
    #        3
    #     5     1
    #   6  2
    # leaf order: [6, 2, 1]

    rootOne = Node(3, False)
    rootOne.left = Node(5, False)
    rootOne.right = Node(1, False)
    rootOne.left.left = Node(6, False)
    rootOne.left.right = Node(2, False)

    leafSimilar(rootOne)
    leafOne = leaves
    leaves = []

    #        7
    #     2     1
    #   6  2
    # leaf order: [6, 2, 1]
    
    rootTwo = Node(7, False)
    rootTwo.left = Node(2, False)
    rootTwo.right = Node(1, False)
    rootTwo.left.left = Node(6, False)
    rootTwo.left.right = Node(2, False)

    leafSimilar(rootTwo)
    leafTwo = leaves
    leaves = []

    # Ternary operator: (false, true)[test]
    print(("False", "True")[leafOne == leafTwo])
    print(leafOne, leafTwo)