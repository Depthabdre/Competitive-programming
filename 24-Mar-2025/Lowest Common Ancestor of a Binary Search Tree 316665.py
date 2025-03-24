# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        is_find = False
        ans = None
        node = root
        p = p.val
        q = q.val
        while not is_find:
            if (node.val > p and node.val < q ) or ( node.val < p and node.val > q):
                return node
            elif node.val > p and node.val > q:
                node = node.left
            elif node.val < p and node.val < q:
                node = node.right
            else:
                return node
        return node
            
