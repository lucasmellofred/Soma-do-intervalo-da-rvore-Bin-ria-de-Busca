class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Main2:
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
    solution = Main2()

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.left.left.left = TreeNode(1)
    root.left.right.left = TreeNode(6)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)

    inicial = 6
    finalValue = 10

    resultado = solution.rangeSum(root, inicial, finalValue)
    print(resultado)  # O resultado será 23
