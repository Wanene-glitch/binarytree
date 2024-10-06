class TreeNode:
    def _init_(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Height:
    def _init_(self):
        self.height = 0

def is_balanced(root, height):
    if root is None:
        height.height = 0
        return True

    left_height = Height()
    right_height = Height()

    l = is_balanced(root.left, left_height)
    r = is_balanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False