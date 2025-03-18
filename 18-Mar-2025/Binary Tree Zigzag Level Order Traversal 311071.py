# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levelElements = deque()
    
        levelElements.append(root)
       
        ans = []
        level = 1  

        while levelElements:
            beforelen = len(levelElements) 
            temp = [node.val for node in levelElements]  
            
            
            if level % 2 == 1:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
                

            
            for _ in range(len(levelElements)):
                node = levelElements.popleft()
                if node.left:
                    levelElements.append(node.left)
                if node.right:
                    levelElements.append(node.right)

            level += 1  

        return ans
        