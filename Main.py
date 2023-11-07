class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Main:
    def rangeSum(self, root, inicial, finalValue):
        if root is None:
            return 0

        if root.val < inicial:
            return self.rangeSum(root.right, inicial, finalValue)
        elif root.val > finalValue:
            return self.rangeSum(root.left, inicial, finalValue)
        else:
            return root.val + self.rangeSum(root.left, inicial, finalValue) + self.rangeSum(root.right, inicial, finalValue)

if __name__ == "__main__":
    solution = Main()

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    inicial = 7
    finalValue = 15

    resultado = solution.rangeSum(root, inicial, finalValue)
    print(resultado) # O resultado será 32
