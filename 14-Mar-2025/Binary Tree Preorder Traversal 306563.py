# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def preord(nodes):
            if not nodes:
                return
            answer.append(nodes.val)
            preord(nodes.left)
            preord(nodes.right)
        preord(root)
        return answer

            
        