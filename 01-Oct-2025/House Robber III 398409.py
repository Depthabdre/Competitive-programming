# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        
        def dp(node, hold):
            if not node:
                return 0
            if (node, hold) in memo:
                return memo[(node, hold)]
            
            if hold:  
               
                ans = dp(node.left, 0) + dp(node.right, 0)
            else:
              
                rob_this = node.val + dp(node.left, 1) + dp(node.right, 1)
                skip_this = dp(node.left, 0) + dp(node.right, 0)
                ans = max(rob_this, skip_this)
            
            memo[(node, hold)] = ans
            return ans
        
        return dp(root, 0)
