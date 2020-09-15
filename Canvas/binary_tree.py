# node class
class Node:
    # constructor
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder(self, start, traversal):
        # root->left->Right

        # check if the given start node is not None
        if start:
            traversal.append(start.data)
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)

        return traversal

    def inorder(self, start, traversal):
        # left->root->right
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal.append(start.data)
            traversal = self.inorder(start.right, traversal)

        return traversal

    def postorder(self, start, traversal):
        # left->right->root
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal.append(start.data)

        return traversal

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(self.root, [])
        elif traversal_type == "inorder":
            return self.inorder(self.root, [])
        elif traversal_type == "postorder":
            return self.postorder(self.root, [])
        else:
            print("Traversal type not supported")
            return False

def main():
    # define a binary tree object
    tree = BinaryTree(1)

    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(tree.print_tree("preorder"))
    print(tree.print_tree("inorder"))
    print(tree.print_tree("postorder"))


if __name__ == '__main__':
    main()
