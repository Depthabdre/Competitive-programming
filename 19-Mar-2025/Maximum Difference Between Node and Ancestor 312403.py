# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def finder(node):
            if not node.left and not node.right:
                return (node.val,node.val,0)

            maxs,maxsr = 0, 0
            ans = 0
            ansr = 0
            mins,minsr = float('inf') , float('inf')
            
            if node.left:
                mins,maxs,ans = finder(node.left)
            if node.right:
                minsr,maxsr,ansr = finder(node.right)

            bestmin , bestmax = min(mins,minsr,node.val) , max(maxs,maxsr,node.val)
            ansfinal = max(ans , ansr , abs(node.val - bestmin) , abs(node.val - bestmax))
            return bestmin , bestmax , ansfinal

        a,b,answer = finder(root)
        return answer

        