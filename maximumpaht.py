class TreeNode:
    def _init_(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def max_gain(node):
            if not node:
                return 0
            
            # Compute the maximum path sum for left and right children
            left_gain = max(max_gain(node.left), 0)  # We only add positive contributions
            right_gain = max(max_gain(node.right), 0)

            # Current path sum includes the node and the best of both subtrees
            current_path_sum = node.value + left_gain + right_gain
            
            # Update the maximum sum if current path sum is greater
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the maximum gain from this node
            return node.value + max(left_gain, right_gain)

        max_gain(root)
        return self.max_sum