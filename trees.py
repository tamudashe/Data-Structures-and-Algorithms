class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.pre_order(self.root, '')
        elif traversal_type == 'inorder':
            return self.in_order(tree.root, '')
        elif traversal_type == 'postorder':
            return self.post_order(tree.root, '')
        else:
            print('traversal type is not supported')
            return False
    
    def pre_order(self, start, traversal):
        # root -> left -> right
        # 1. check if the node given is None
        if start:
            traversal += (str(start.data) + '-')
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal
            
    def in_order(self, start, traversal):
        # left -> root -> right
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal += (str(start.data) + '-')
            traversal = self.in_order(start.right, traversal)
        return traversal

    def post_order(self, start, traversal):
        # left -> right -> root
        if start:
            traversal = self.post_order(start.left, traversal)
            traversal = self.post_order(start.right, traversal)
            traversal += (str(start.data) + '-')
        return traversal
    
    def bfs(self):
        pass 
    
    
tree = BinaryTree(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
print(tree.print_tree('postorder'))

