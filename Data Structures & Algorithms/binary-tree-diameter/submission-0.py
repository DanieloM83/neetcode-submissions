# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(node):
            nonlocal answer
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            
            left = dfs(node.left)
            right = dfs(node.right)

            answer = max(answer, left + right)

            return max(left, right) + 1
        dfs(root)
        return answer