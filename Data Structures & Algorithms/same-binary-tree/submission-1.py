# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None:
            return q is None
        if q is None:
            return p is None
        nodes_p = [p.val]
        nodes_q = [q.val]

        def dfs(node, nodes):
            if node is None:
                return
            if node.left:
                nodes.append(node.left.val)
            else:
                nodes.append(None)
            if node.right:
                nodes.append(node.right.val)
            else:
                nodes.append(None)
            
            dfs(node.left, nodes)
            dfs(node.right, nodes)

        dfs(p, nodes_p)
        dfs(q, nodes_q)

        return nodes_p == nodes_q