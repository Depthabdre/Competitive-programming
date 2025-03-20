# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            node = TreeNode(val)
            return node
        
        else:
            node = root
            while node:
                if node.val > val:
                    prev = node
                    node = node.left
                else:
                    prev = node
                    node = node.right
            
            temp = TreeNode(val)
            if prev.val > val:
                prev.left = temp
            else:
                prev.right = temp
        return root

        