import random

class BinaryTree:
    def __init__(self, value: int):
        self.key = value
        self.left = None
        self.right = None
        self.result = []
    
    def add(self, value: int):
        if self.key is None:
            self.key = value
            return
        else:
            if value > self.key:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.add(value)
            elif value < self.key:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.add(value)
            else:
                raise "Error"
    
    def output(self, branch = 'root', level = 0):
        print(f'Branch = {branch} ---- Level = {level} ---- key = {self.key}')
        if self.left is not None:
            self.left.output('left', level + 1)
        if self.left is not None:
            self.right.output('right', level + 1)

    def in_order_rec(self, tree):
        if tree:
            self.in_order_rec(tree.left)
            print(tree.key, end=", ")
            self.in_order_rec(tree.right)

    def in_order_iter(self, tree):
        stack = []
        while stack or tree:
            if tree:
                stack.append(tree)
                tree = tree.left
            else:
                tree = stack.pop()
                print(tree.key, end=', ')
                tree = tree.right
        
        



Tree = BinaryTree(75)

array = set([random.randint(0, 50) for i in range(50)])

for i in array:
    Tree.add(i)

Tree.in_order_iter(Tree)
