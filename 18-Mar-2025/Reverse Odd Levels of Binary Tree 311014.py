# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        levelElements = deque()
        if root.left:
            levelElements.append(root.left)
            levelElements.append(root.right)

        level = 1  

        while levelElements:
            beforelen = len(levelElements) // 2
            temp = list(levelElements)  
            
            
            if level % 2 == 1:
                for i in range(beforelen):
                    temp[i].val, temp[-(i + 1)].val = temp[-(i + 1)].val, temp[i].val

            
            for _ in range(len(levelElements)):
                node = levelElements.popleft()
                if node.left:
                    levelElements.append(node.left)
                    levelElements.append(node.right)

            level += 1  

        return root
