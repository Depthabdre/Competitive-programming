# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        parent = None
        node = root

        
        while node and node.val != key:
            parent = node
            if key < node.val:
                node = node.left
            else:
                node = node.right

        
        if not node:
            return root

        
        if not node.left and not node.right:  
            if not parent:
                return None 
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None

        elif node.left and not node.right:  
            if not parent:
                return node.left  
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left

        elif not node.left and node.right:  
            if not parent:
                return node.right  
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right

        else: 
            min_parent = node
            min_node = node.right
            while min_node.left:
                min_parent = min_node
                min_node = min_node.left

            
            node.val = min_node.val

            
            if min_parent.left == min_node:
                min_parent.left = min_node.right
            else:
                min_parent.right = min_node.right

        return root
