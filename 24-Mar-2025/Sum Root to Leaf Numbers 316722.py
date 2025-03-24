# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        prev = root.val
        node = root
        ans = []
        prev = 0
        def depth(node,prev):
            if not node:
                return
            if node and not node.right and not node.left:
                prev *= 10
                prev += node.val
                ans.append(prev) 
                prev //= 10
                return 
            prev *= 10
            prev += node.val

            depth(node.left,prev)
            depth(node.right,prev)
            prev //= 10
        
        depth(node , prev)
        
        return sum(ans)
             
        




        