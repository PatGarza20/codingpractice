## Function to find the number of cycles in a given graph.

cycles = 0

class Node:
    def __init__(self,val,visited):
        self.val = val
        self.visited = visited
        self.left = None
        self.right = None

def hasCycle(root, parent):
    global cycles

    root.visited = True

    # If a neighboring node has been visited and isn't the parent, adds to cycles.
    if root.left != None:
        if root.left.visited == False:
            hasCycle(root.left, root)
        elif parent.val != root.left.val:
            cycles += 1
    
    if root.right != None:
        if root.right.visited == False:
            hasCycle(root.right, root)
        elif parent.val != root.right.val:
            cycles += 1


if __name__ == "__main__":
    root = Node(0, False)
    root.left = Node(1, False)
    root.right = Node(2, False)
    root.left.left = root
    root.left.right = root.right
    root.right.left = root.left
    root.right.right = root

    hasCycle(root, root)
    print(cycles//2, "Cycle")