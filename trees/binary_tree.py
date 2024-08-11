# This Node class represents a single node in a binary tree.
# Each node contains a value (val) and pointers to its left and right children.
class Node:
    def __init__(self, key):
        # Initialize the node with a key (value) and set the left and right children to None.
        self.left = None
        self.right = None
        self.val = key

# This function performs an inorder traversal of the binary tree.
# Inorder traversal visits the left subtree, the root node, and then the right subtree.
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)   # Recursively visit the left subtree.
        print(root.val, end=' ')       # Print the root node's value.
        inorder_traversal(root.right)  # Recursively visit the right subtree.

# This function inserts a new node with a specified key into the binary tree.
# It maintains the binary search tree property, where left children are less than the parent, and right children are greater.
def insert(root, key):
    # If the tree is empty, return a new node as the root.
    if root is None:
        return Node(key)
    else:
        # If the key is greater than the root's value, insert it into the right subtree.
        if root.val < key:
            root.right = insert(root.right, key)
        # If the key is less than or equal to the root's value, insert it into the left subtree.
        else:
            root.left = insert(root.left, key)
    return root

# Example usage:
if __name__ == "__main__":
    # Create the root of the binary tree with value 50.
    r = Node(50)
    # Insert nodes into the binary tree.
    r = insert(r, 30)
    r = insert(r, 20)
    r = insert(r, 40)
    r = insert(r, 70)
    r = insert(r, 60)
    r = insert(r, 80)

    # Print the inorder traversal of the binary tree.
    print("Inorder traversal of the binary tree:")
    inorder_traversal(r)
