## Function to find the depth of a binary search tree.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Recursively iterates through each node and returns the greatest value with max().
def getDepth(root):
    if root == None:
        return 0

    return max(getDepth(root.left) + 1, getDepth(root.right) + 1)

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(20)
    root.left.left = Node(5)
    root.left.right = Node(9)
    root.right.right = Node(30)
    root.right.left = Node(15)

    #        10
    #     8     20
    #   5  9  15  30

    print("Depth:", getDepth(root))