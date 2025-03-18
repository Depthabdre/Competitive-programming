# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        levelElements = deque()
        if root:levelElements.append(root)
        ans = []
        while levelElements:
            maxele = float('-inf')
            beforelen = len(levelElements)
            for i in range(beforelen):
                node = levelElements.popleft()

                maxele = max(maxele, node.val) 

                if node.left:
                    levelElements.append(node.left)
                if node.right:
                    levelElements.append(node.right)

            ans.append(maxele)
        return ans


