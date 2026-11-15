# This Node class represents a single node in a binary tree.
# Each node contains a value (val) and pointers to its left and right children.
class Node:
    def __init__(self, key):
        # Initialize the node with a key (value) and set the left and right children to None.
        self.left = None
        self.right = None
        self.val = key

# This BinaryTree class provides a structure to manage the binary tree operations.
class BinaryTree:
    def __init__(self):
        # Initialize the root of the binary tree as None.
        self.root = None

    # This method inserts a new node with a specified key into the binary tree.
    def insert(self, key):
        # Use the helper function to insert into the tree.
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self._insert(root.right, key)
            else:
                root.left = self._insert(root.left, key)
        return root

    # This method performs an inorder traversal of the binary tree.
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.val)
            self._inorder_traversal(root.right, result)


def layout(tree):
    """Positions for drawing the tree.

    Returns (nodes, edges): nodes is a list of (value, column, depth), where the
    column is the node's place in in-order order, so a left child is always
    drawn left of its parent; edges is a list of (parent index, child index)
    into that list.
    """
    nodes, edges = [], []

    def walk(node, depth):
        if node is None:
            return None
        left = walk(node.left, depth + 1)
        me = len(nodes)
        nodes.append((node.val, me, depth))
        right = walk(node.right, depth + 1)
        for child in (left, right):
            if child is not None:
                edges.append((me, child))
        return me

    walk(tree.root, 0)
    return nodes, edges
