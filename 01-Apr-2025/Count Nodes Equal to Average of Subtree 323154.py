# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return (0, 0, 0)
            
            left_sum, left_count, left_match = dfs(node.left)
            right_sum, right_count, right_match = dfs(node.right)
            
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            match = left_match + right_match + (1 if node.val == total_sum // total_count else 0)
            
            return (total_sum, total_count, match)
        
        return dfs(root)[2]
