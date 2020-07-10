## Function to return the longest path from root to leaf in a binary tree.

class Node: 
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

longest = ""
def longestPath(root, path):
    global longest 
    
    if len(path) > len(longest):
        longest = path

    if root.left != None:
        longestPath(root.left, path + str(root.left.val))
    if root.right != None:
        longestPath(root.right, path + str(root.right.val))

if __name__ == "__main__":
    #    1
    #  /   \
    # 3     2
    #  \   /
    #   5 4
    #  /
    # 6

    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.right.left = Node(4)
    root.left.right = Node(5)
    root.left.right.left = Node(6)

    # Starts with the root's value already in path.
    # prints [1, 3, 5, 6]
    longestPath(root, str(root.val))
    print(list(longest))
