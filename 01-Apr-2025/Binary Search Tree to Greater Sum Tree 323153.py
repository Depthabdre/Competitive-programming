# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = [0]
        
        def reverse_inorder(node, total):
            if not node:
                return
            
            reverse_inorder(node.right, total)
            total[0] += node.val
            node.val = total[0]
            reverse_inorder(node.left, total)
        
        reverse_inorder(root, total)
        return root

        