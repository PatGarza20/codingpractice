## Function for BFS/DFS on a binary search tree.

class Node:
    def __init__(self, val, visited):
        self.val = val
        self.visited = visited
        self.left = None
        self.right = None

# Uses a while loop and a Queue to perform BFS.
def BFS(root):
    if root == None:
        return ""

    queue = [root]
    root.visited = True

    while queue:
        current = queue.pop(0)
        print(current.val)

        if current.left != None:
            if current.left.visited == False:
                current.left.visited == True
                queue.append(current.left)

        if current.right != None:
            if current.right.visited == False:
                current.right.visited == True
                queue.append(current.right)
            
# Uses recursion and a Stack to perform DFS.
def DFS(root):
    if root == None:
        return ""
        
    stack = [root]
    root.visited = True
    
    print(root.val)

    if root.left != None:
        stack.append(root.left)
    if root.right != None:
        stack.append(root.right)

    for node in stack:
        if node.visited == False:
            node.visited = True
            DFS(node)

if __name__ == "__main__":
    root = Node(10, False)
    root.left = Node(8, False)
    root.right = Node(20, False)
    root.left.left = Node(5, False)
    root.left.right = Node(9, False)
    root.right.right = Node(30, False)
    root.right.left = Node(15, False)

    #        10
    #     8     20
    #   5  9  15  30

    print("BFS:")   
    BFS(root)
    print("\nDFS:")
    DFS(root)