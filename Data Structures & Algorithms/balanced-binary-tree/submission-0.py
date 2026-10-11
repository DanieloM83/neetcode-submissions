# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return (0, True)
            if node.left is None and node.right is None:
                return (1, True)
            
            left = height(node.left)
            right = height(node.right)

            is_balanced = (abs(left[0] - right[0]) <= 1) and left[1] and right[1]

            return (max(left[0], right[0]) + 1, is_balanced)
        
        return height(root)[1]