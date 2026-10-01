# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        def depth(node, i):
            if node is None: return i
            answer = max(depth(node.left, i+1), depth(node.right, i+1))
            return answer
        
        answer = max(depth(root.left, 1), depth(root.right, 1))
        return answer